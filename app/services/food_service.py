from app.extensions import SessionLocal
from app.models.food import Food
from app.models.request_log import RequestLog
from app.services.llm_service import generate_from_llm
from app.utils.parser import parse_llm_response

def create_foods(theme: str, total: int):
    session = SessionLocal()

    try:
        # Prompt disesuaikan untuk tema makanan (Food)
        prompt = f"""
        Dalam format JSON, buat {total} deskripsi makanan dengan tema "{theme}".
        Format:
        {{
            "foods": [
                {{"description": "..."}}
            ]
        }}
        """

        result = generate_from_llm(prompt)
        foods = parse_llm_response(result)

        # save request log
        req_log = RequestLog(theme=theme)
        session.add(req_log)
        session.commit()

        saved = []

        for item in foods:
            # Mengambil key 'description' sesuai perubahan pada model sebelumnya
            description = item.get("description")

            f = Food(
                description=description,
                request_id=req_log.id
            )
            session.add(f)
            saved.append(description)

        session.commit()

        return saved

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()


def get_all_foods(page: int = 1, per_page: int = 100):
    session = SessionLocal()

    try:
        query = session.query(Food)

        total = query.count()

        data = (
            query
            .order_by(Food.id.desc())
            .offset((page - 1) * per_page)
            .limit(per_page)
            .all()
        )

        result = [
            {
                "id": f.id,
                "description": f.description,
                "created_at": f.created_at.isoformat()
            }
            for f in data
        ]

        return {
            "page": page,
            "per_page": per_page,
            "total": total,
            "total_pages": (total + per_page - 1) // per_page,
            "data": result
        }

    finally:
        session.close()
from sqlalchemy import select, update

from models_postgres import Author as postAuthor, Quote as postQuote, session


quotes = session.execute(
            select(postQuote.id, postQuote.tags)
        ).fetchall()


for quote in quotes:
    
    new_tags = quote.tags.replace("{","").replace("}", "")
    
    print(new_tags)
    
    session.execute(update(postQuote)
                    .where(postQuote.id==quote.id)
                    .values(tags=new_tags))
    # print(f"{a=}")
    # session.add(a)
session.commit()
    # input("++++++++++")
class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text = text
        self.page = page
        self.date = date

    def __str__(self) -> str:
        return f"{self.date} - page {self.page}: {self.text}"


class Book:
    EXCELLENT = 3
    GOOD = 2
    BAD = 1
    UNRATED = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn:str  = isbn
        self.title:str = title
        self.author:str = author
        self.pages : int= pages
        self.rating:int = Book.UNRATED
        self.notes: listz[Note] = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        note = Note(text, page, date)
        self.notes.append(note)
        return True

    def set_rating(self, rating: int) -> bool:
        if rating not in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            return False
        self.rating = rating
        return True

    def get_notes_of_page(self, page: int) -> List[Note]:
        return [note for note in self.notes if note.page == page]

    def page_with_most_notes(self) -> int:
        if not self.notes:
            return -1

        note_count = {}
        for note in self.notes:
            note_count[note.page] = note_count.get(note.page, 0) + 1

        return max(note_count, key=note_count.ge
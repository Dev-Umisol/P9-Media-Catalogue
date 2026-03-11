# 📁 Media Catalogue
> A Python OOP project that models a media catalogue supporting both movies and TV series — with inheritance, custom exceptions, and list comprehensions.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)

## 📌 About
This project was built to practise inheritance, custom exceptions, and list comprehensions in Python. A `Movie` parent class defines shared attributes, `TVSeries` extends it with season and episode data, and `MediaCatalogue` acts as a container that stores, filters, and displays both types. All validation is handled through `raise` statements, and a custom `MediaError` exception provides richer error context when invalid objects are added.

## 🧠 What I Learned

- **Inheritance with `super()`** — `TVSeries` extends `Movie` by calling `super().__init__()` to reuse the parent's validation and attributes, then adding its own (`seasons`, `total_episodes`) on top
- **Custom exceptions** — Creating `MediaError` by subclassing `Exception` and adding an `obj` attribute, so the error carries not just a message but a reference to the object that caused it
- **`type()` vs `isinstance()` in list comprehensions** — Using `type(item) is Movie` (not `isinstance`) to filter strictly by class, ensuring `TVSeries` objects don't appear in the movies list even though they inherit from `Movie`
- **List comprehensions** — Replacing verbose for loops with concise one-liners like `[item for item in self.items if type(item) is Movie]` to filter the catalogue
- **`enumerate()` with `start=1`** — Numbering catalogue output from 1 for a clean, user-friendly display
- **Docstrings** — Adding `"""docstrings"""` to each class to document their purpose, accessible at runtime via __doc__
- **`try/except` with multiple exception types** — Catching `ValueError` and `MediaError` separately in the same block to handle different failure modes with different messages

## 🛠️ Technologies Used
| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x | Core Language |

## 💡 How It Works

Three classes work together to model the system:

- `Movie` — Base class with title, year, director, and duration validation
- `TVSeries` — Extends `Movie` with seasons and total episodes
- `MediaCatalogue` — Stores any `Movie` or `TVSeries` instance and can filter and display them separately

**Example Output:**
```
Media Catalogue (4 items):

=== MOVIES ===
1. Swiss Army Man (2016) - 97 min, Daniel Scheinert and Daniel Kwan
2. The Matrix (1999) - 136 min, The Wachowskis

=== TV SERIES ===
1. The Flash (2014) - 9 seasons, 184 episodes, 30 min avg, Greg Berlanti...
2. Scrubs (2001) - 9 seasons, 182 episodes, 24 min avg, Bill Lawrence
```

## 🚀 Future Improvements

- [ ]  Add a search(title) method to find items by name
- [ ]  Add a DocumentaryFilm subclass to extend the catalogue further
- [ ]  Sort the catalogue by year, title, or duration
- [ ]  Save and load the catalogue from a JSON file for persistence

## 📂 Project Structure

```
media-catalogue/
│
├── P9MediaCatalogue.py    # Movie, TVSeries, MediaCatalogue classes and demo
└── README.md
```

*Part of my Python learning journey 🐍 — practicing inheritance, custom exceptions, and list comprehensions*

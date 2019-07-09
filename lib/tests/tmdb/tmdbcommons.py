JSON = {
    "page": 1,
    "total_results": 2,
    "total_pages": 1,
    "results": [
        {
            "original_name": "Stranger Things",
            "id": 66732,
            "name": "Stranger Things",
            "vote_count": 2360,
            "vote_average": 8.3,
            "poster_path": "/x2LSRK2Cm7MZhjluni1msVJ3wDF.jpg",
            "first_air_date": "2016-07-15",
            "popularity": 492.715,
            "genre_ids": [
                18,
                9648,
                10765
            ],
            "original_language": "en",
            "backdrop_path": "/56v2KjBlU4XaOv9rVYEQypROD7P.jpg",
            "overview": "When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces, and one strange little girl.",
            "origin_country": [
                "US"
            ]
        },
        {
            "original_name": "Beyond Stranger Things",
            "id": 74851,
            "name": "Beyond Stranger Things",
            "vote_count": 17,
            "vote_average": 7.5,
            "poster_path": "/pixcHLGqLYuMMHdRHmIC0oLsgbp.jpg",
            "first_air_date": "2017-10-27",
            "popularity": 7.099,
            "genre_ids": [
                10767
            ],
            "original_language": "en",
            "backdrop_path": "/qevaCqIekzc7Bp5f2kGAi92kO39.jpg",
            "overview": "Secrets from the \"Stranger Things 2\" universe are revealed as cast and guests discuss the latest episodes with host Jim Rash. Caution: spoilers ahead!",
            "origin_country": []
        }
    ]
}

TV_SHOW = 'Stranger Things'
API_KEY = 'ae3d0eb6baf8bffc074dbb90b8f764ba'
URL = 'https://api.themoviedb.org/3/search/tv'
URL += f'?api_key={API_KEY}&query={TV_SHOW.replace(" ", "%20")}'

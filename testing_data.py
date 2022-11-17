"""Data for unit testing.  Kept in a separate file to cleanliness"""

search_results = """{
  "_links": {
    "next": {
      "href": "https://api.edamam.com/api/recipes/v2?q=curry&app_key=b7db63449d8aef2259fb1681f9fb9a75&_cont=CHcVQBtNNQphDmgVQntAEX4BYVVtBQYBQWxDAGIXZ1FwBwUVX3dAVmEWYFJyAQQOQ2wWCzAaalV0UAUOQGNBBWdCYVNwBRFqX3cWQT1OcV9xBB8VADQWVhFCPwoxXVZEITQeVDcBaR4-SQ%3D%3D&type=public&app_id=2b4bf0c3",
      "title": "Next page"
    }
  },
  "count": 10000,
  "from": 1,
  "hits": [
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/61c68c5e83feda078d4cd2f178a8aba3?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 1131.6555772794445,
        "cautions": [
          "Gluten",
          "Wheat",
          "Sulfites",
          "FODMAP"
        ],
        "cuisineType": [
          "asian"
        ],
        "dietLabels": [
          "High-Fiber",
          "Low-Sodium"
        ],
        "digest": [
          {
            "daily": 95.96031022140622,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 51.9415946107993,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 10.388318922159861,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 35.84029633942445,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 12.895446084551736,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 62.374201643914034,
            "unit": "g"
          },
          {
            "daily": 36.41891343122477,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 80.35983379031126,
                "unit": "g"
              },
              {
                "daily": 115.58762601345222,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 28.896906503363056,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 30.403512396724306,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 109.25674029367431,
            "unit": "g"
          },
          {
            "daily": 107.17917340517417,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 53.589586702587084,
            "unit": "g"
          },
          {
            "daily": 0.49064993962666664,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 1.47194981888,
            "unit": "mg"
          },
          {
            "daily": 14.486248915774308,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 347.66997397858336,
            "unit": "mg"
          },
          {
            "daily": 112.07598602961362,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 1120.7598602961361,
            "unit": "mg"
          },
          {
            "daily": 89.49033414167064,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 375.85940339501667,
            "unit": "mg"
          },
          {
            "daily": 71.28836833337087,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 3350.5533116684305,
            "unit": "mg"
          },
          {
            "daily": 72.5690513709051,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 13.062429246762918,
            "unit": "mg"
          },
          {
            "daily": 62.90122349,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 6.9191345839,
            "unit": "mg"
          },
          {
            "daily": 144.13880757240676,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 1008.9716530068473,
            "unit": "mg"
          },
          {
            "daily": 11.52259275083889,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 103.70333475755,
            "unit": "\u00b5g"
          },
          {
            "daily": 361.22493319751544,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 325.1024398777639,
            "unit": "mg"
          },
          {
            "daily": 262.12553323381366,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 3.1455063988057637,
            "unit": "mg"
          },
          {
            "daily": 69.59795276546474,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.9047733859510415,
            "unit": "mg"
          },
          {
            "daily": 59.38274792991146,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 9.501239668785834,
            "unit": "mg"
          },
          {
            "daily": 171.45340220849891,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 2.228894228710486,
            "unit": "mg"
          },
          {
            "daily": 114.38727899210834,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 457.54911596843334,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 457.54911596843334,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.18009967999999998,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.004322392319999999,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 62.40886945080648,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 9.361330417620971,
            "unit": "mg"
          },
          {
            "daily": 110.2528377720817,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 132.30340532649805,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 1509.0518920488187,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Vegan",
          "Vegetarian",
          "Pescatarian",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/c24/c24d5879c21826517f3aa9bca10e4250.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=9b9bd5d35029b5abc472bdea542c6a513fbb9fe70232946a396f4383378be0b9",
        "images": {
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/c24/c24d5879c21826517f3aa9bca10e4250.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=9b9bd5d35029b5abc472bdea542c6a513fbb9fe70232946a396f4383378be0b9",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/c24/c24d5879c21826517f3aa9bca10e4250-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=7e19f775637a8d088bfddc9c294e0228d16f7b5bc4ba24d57f47672c302bc23f",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/c24/c24d5879c21826517f3aa9bca10e4250-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=77f8652c22ed506edf10680c94b794f538dd6ef766e76e51d44652d8188d5ce8",
            "width": 100
          }
        },
        "ingredientLines": [
          "3 tablespoons olive oil",
          "1 large yellow onion, finely chopped",
          "1 14-ounce package extra-firm tofu, drained, patted dry, and cut into 3/4-inch dice",
          "1 heaping tablespoon hot curry or vindaloo curry paste",
          "1 14.5-ounce can diced tomatoes",
          "1 head cauliflower, cut into 3/4-inch florets",
          "Cooked brown basmati rice, for serving"
        ],
        "ingredients": [
          {
            "food": "olive oil",
            "foodCategory": "Oils",
            "foodId": "food_b1d1icuad3iktrbqby0hiagafaz7",
            "image": "https://www.edamam.com/food-img/4d6/4d651eaa8a353647746290c7a9b29d84.jpg",
            "measure": "tablespoon",
            "quantity": 3.0,
            "text": "3 tablespoons olive oil",
            "weight": 40.5
          },
          {
            "food": "yellow onion",
            "foodCategory": "vegetables",
            "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
            "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 large yellow onion, finely chopped",
            "weight": 150.0
          },
          {
            "food": "tofu",
            "foodCategory": "plant-based protein",
            "foodId": "food_a269ixea1yf51xbfwgnq2boiwc7x",
            "image": "https://www.edamam.com/food-img/b6a/b6ae13c3cfe37e16f820840f90231bff.jpg",
            "measure": "ounce",
            "quantity": 14.0,
            "text": "1 14-ounce package extra-firm tofu, drained, patted dry, and cut into 3/4-inch dice",
            "weight": 396.89332375000004
          },
          {
            "food": "curry paste",
            "foodCategory": "condiments and sauces",
            "foodId": "food_aojdol2are6zg7af2nincbe87jot",
            "image": "https://www.edamam.com/food-img/b6a/b6a9ebae5850f42eca0253827603ef9c.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 heaping tablespoon hot curry or vindaloo curry paste",
            "weight": 16.0
          },
          {
            "food": "can diced tomatoes",
            "foodCategory": "canned vegetables",
            "foodId": "food_a0edr25b8gjzxdbxcvus4blkd8b8",
            "image": "https://www.edamam.com/food-img/645/6455f54947348b60ec6557fcc0ef5121.jpeg",
            "measure": "ounce",
            "quantity": 14.5,
            "text": "1 14.5-ounce can diced tomatoes",
            "weight": 411.0680853125
          },
          {
            "food": "cauliflower",
            "foodCategory": "vegetables",
            "foodId": "food_buqfaxubzh6hi5asev8a5aj9sr71",
            "image": "https://www.edamam.com/food-img/ca2/ca217d31067dffd35ce1215e7f336bd8.jpg",
            "measure": "head",
            "quantity": 1.0,
            "text": "1 head cauliflower, cut into 3/4-inch florets",
            "weight": 537.7777777777777
          },
          {
            "food": "Cooked brown basmati rice",
            "foodCategory": "grains",
            "foodId": "food_aaqvgp7bc30zo8bjip7uga0bibmh",
            "image": "https://www.edamam.com/food-img/663/6630da3c48c2df8fcd86eddda231beb3.jpg",
            "measure": "serving",
            "quantity": 1.0,
            "text": "Cooked brown basmati rice, for serving",
            "weight": 195.0
          }
        ],
        "label": "Cauliflower and Tofu Curry Recipe",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/cauliflower-and-tofu-curry-recipe-61c68c5e83feda078d4cd2f178a8aba3/curry",
        "source": "Serious Eats",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 112.07598602961362,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 36.41891343122477,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.49064993962666664,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 56.58277886397223,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 51.9415946107993,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 95.96031022140622,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 72.5690513709051,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 115.58762601345222,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 114.38727899210834,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 71.28836833337087,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 89.49033414167064,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 14.486248915774308,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 59.38274792991146,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 144.13880757240676,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 107.17917340517417,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 69.59795276546474,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 262.12553323381366,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 62.40886945080648,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 11.52259275083889,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.18009967999999998,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 171.45340220849891,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 361.22493319751544,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 110.2528377720817,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 62.90122349,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 1120.7598602961361,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 109.25674029367431,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 80.35983379031126,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 1.47194981888,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 1131.6555772794445,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 35.84029633942445,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 12.895446084551736,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 10.388318922159861,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 62.374201643914034,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 13.062429246762918,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 28.896906503363056,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 457.54911596843334,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 457.54911596843334,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 3350.5533116684305,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 375.85940339501667,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 347.66997397858336,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 9.501239668785834,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 1008.9716530068473,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 53.589586702587084,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.9047733859510415,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 30.403512396724306,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 3.1455063988057637,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 9.361330417620971,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 103.70333475755,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.004322392319999999,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 2.228894228710486,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 325.1024398777639,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 132.30340532649805,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 1509.0518920488187,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 6.9191345839,
            "unit": "mg"
          }
        },
        "totalTime": 50.0,
        "totalWeight": 1747.2391868402779,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_61c68c5e83feda078d4cd2f178a8aba3",
        "url": "http://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html",
        "yield": 4.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/b8d126947d802def1f795016d75297c4?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 716.9749125599999,
        "cautions": [
          "Sulfites",
          "FODMAP"
        ],
        "cuisineType": [
          "south east asian"
        ],
        "dietLabels": [
          "High-Protein",
          "Low-Fat"
        ],
        "digest": [
          {
            "daily": 18.04015700381538,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 17.615726390399995,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 3.5231452780799994,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.022619999999999998,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 3.2722975116799997,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 3.3014249792,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 11.726102052479998,
            "unit": "g"
          },
          {
            "daily": 17.396341668799998,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 46.134007593279996,
                "unit": "g"
              },
              {
                "daily": 24.220069652480003,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 6.05501741312,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 6.4998607232,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 52.189025006399994,
            "unit": "g"
          },
          {
            "daily": 207.59370456031996,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 103.79685228015998,
            "unit": "g"
          },
          {
            "daily": 77.82398327295999,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 233.47194981887998,
            "unit": "mg"
          },
          {
            "daily": 31.900943052666662,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 765.6226332639999,
            "unit": "mg"
          },
          {
            "daily": 19.88557002944,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 198.8557002944,
            "unit": "mg"
          },
          {
            "daily": 42.103666288,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 176.83539840959997,
            "unit": "mg"
          },
          {
            "daily": 35.966182851404255,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 1690.410594016,
            "unit": "mg"
          },
          {
            "daily": 37.48106656355556,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 6.74659198144,
            "unit": "mg"
          },
          {
            "daily": 25.784893585454544,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 2.8363382944,
            "unit": "mg"
          },
          {
            "daily": 135.33813350628571,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 947.366934544,
            "unit": "mg"
          },
          {
            "daily": 1.623150665422222,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 14.6083559888,
            "unit": "\u00b5g"
          },
          {
            "daily": 24.30687288,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 21.876185592000002,
            "unit": "mg"
          },
          {
            "daily": 49.169168760000005,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.59003002512,
            "unit": "mg"
          },
          {
            "daily": 41.73511372307692,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.5425564784,
            "unit": "mg"
          },
          {
            "daily": 146.417245694,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 23.42675931104,
            "unit": "mg"
          },
          {
            "daily": 70.43179100307692,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 0.91561328304,
            "unit": "mg"
          },
          {
            "daily": 52.317651074400004,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 209.2706042976,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 179.69060429759998,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 17.4,
            "unit": "\u00b5g"
          },
          {
            "daily": 305.64676634666665,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 7.33552239232,
            "unit": "\u00b5g"
          },
          {
            "daily": 95.89333333333333,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 14.383999999999999,
            "unit": "\u00b5g"
          },
          {
            "daily": 16.410447731199998,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 2.46156715968,
            "unit": "mg"
          },
          {
            "daily": 10.4261962724,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 12.51143552688,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 463.13090268959996,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Sugar-Conscious",
          "Pescatarian",
          "Dairy-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Sulfite-Free",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/5e3/5e367b107d760d0c0be9e409c0ab07dd.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d0e8efaf30a739ac03f6dc9aab331dc094d1a1e77fc8452e5d13369be0db4e01",
        "images": {
          "LARGE": {
            "height": 600,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/5e3/5e367b107d760d0c0be9e409c0ab07dd-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=34a2d83262424af45b34d15c8ec201e8113ce806339591b731a2dd76821ad1dc",
            "width": 600
          },
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/5e3/5e367b107d760d0c0be9e409c0ab07dd.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d0e8efaf30a739ac03f6dc9aab331dc094d1a1e77fc8452e5d13369be0db4e01",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/5e3/5e367b107d760d0c0be9e409c0ab07dd-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=12fbb36715ee370763f2fe2c814abb7eade858e620a02243f798ddbea91798dd",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/5e3/5e367b107d760d0c0be9e409c0ab07dd-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=61e8c24e83a3c00799c7e7ba3d69bdaab4fc608b69e280b4e1a164b5cd2bce47",
            "width": 100
          }
        },
        "ingredientLines": [
          "3 slices bread , about 85g/3oz in total",
          "1 lime",
          "1.0 tbsp Korma curry paste",
          "4 thick white fish fillets"
        ],
        "ingredients": [
          {
            "food": "bread",
            "foodCategory": "bread, rolls and tortillas",
            "foodId": "food_a3049hmbqj5wstaeeb3udaz6uaqv",
            "image": "https://www.edamam.com/food-img/886/886960f6ce6ccec5b9163bacf2996853.jpg",
            "measure": "slice",
            "quantity": 3.0,
            "text": "3 slices bread , about 85g/3oz in total",
            "weight": 87.0
          },
          {
            "food": "lime",
            "foodCategory": "fruit",
            "foodId": "food_av58muyb8kg92fbk0g8g8aui5knv",
            "image": "https://www.edamam.com/food-img/48a/48a123c9576647c4ada6a41df5eeb22a.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 lime",
            "weight": 67.0
          },
          {
            "food": "curry paste",
            "foodCategory": "condiments and sauces",
            "foodId": "food_aojdol2are6zg7af2nincbe87jot",
            "image": "https://www.edamam.com/food-img/b6a/b6a9ebae5850f42eca0253827603ef9c.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1.0 tbsp Korma curry paste",
            "weight": 16.0
          },
          {
            "food": "fish",
            "foodCategory": "seafood",
            "foodId": "food_ar6pjbvaxqtlqia7jewa4brld7p9",
            "image": "https://www.edamam.com/food-img/717/717cb400eb49626bb7c95cd29292cef4.jpg",
            "measure": "fillet",
            "quantity": 4.0,
            "text": "4 thick white fish fillets",
            "weight": 464.0
          }
        ],
        "label": "Curry-Crusted Fish",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/curry-crusted-fish-b8d126947d802def1f795016d75297c4/curry",
        "source": "BBC Good Food",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 19.88557002944,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 17.396341668799998,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 77.82398327295999,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 35.848745627999996,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 17.615726390399995,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 18.04015700381538,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 37.48106656355556,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 24.220069652480003,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 52.317651074400004,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 35.966182851404255,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 42.103666288,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 31.900943052666662,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 146.417245694,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 135.33813350628571,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 207.59370456031996,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 41.73511372307692,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 49.169168760000005,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 16.410447731199998,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 1.623150665422222,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 305.64676634666665,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 70.43179100307692,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 24.30687288,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 95.89333333333333,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 10.4261962724,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 25.784893585454544,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 198.8557002944,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 52.189025006399994,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 46.134007593279996,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 233.47194981887998,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 716.9749125599999,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 3.2722975116799997,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 3.3014249792,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 3.5231452780799994,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 11.726102052479998,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.022619999999999998,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 6.74659198144,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 6.05501741312,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 17.4,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 209.2706042976,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 179.69060429759998,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 1690.410594016,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 176.83539840959997,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 765.6226332639999,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 23.42675931104,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 947.366934544,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 103.79685228015998,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.5425564784,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 6.4998607232,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.59003002512,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 2.46156715968,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 14.6083559888,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 7.33552239232,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 0.91561328304,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 21.876185592000002,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 14.383999999999999,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 12.51143552688,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 463.13090268959996,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 2.8363382944,
            "unit": "mg"
          }
        },
        "totalTime": 0.0,
        "totalWeight": 634.0,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_b8d126947d802def1f795016d75297c4",
        "url": "http://www.bbcgoodfood.com/recipes/4717/",
        "yield": 4.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/3886b0a75bb05ac5beec1106fb318a4a?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 631.9444444444443,
        "cautions": [
          "Sulfites"
        ],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [
          "Balanced"
        ],
        "digest": [
          {
            "daily": 42.078581196581204,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 48.73440555555556,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 9.746881111111112,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.20632500000000004,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 8.560284444444445,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 4.4929161111111116,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 27.351077777777782,
            "unit": "g"
          },
          {
            "daily": 25.462001851851852,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 62.41445,
                "unit": "g"
              },
              {
                "daily": 55.886222222222216,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 13.971555555555554,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 14.282355555555554,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 76.38600555555556,
            "unit": "g"
          },
          {
            "daily": 54.05206666666666,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 27.02603333333333,
            "unit": "g"
          },
          {
            "daily": 14.083333333333334,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 42.25,
            "unit": "mg"
          },
          {
            "daily": 111.67555555555558,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 2680.2133333333336,
            "unit": "mg"
          },
          {
            "daily": 36.07661111111111,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 360.7661111111111,
            "unit": "mg"
          },
          {
            "daily": 28.743253968253967,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 120.72166666666666,
            "unit": "mg"
          },
          {
            "daily": 39.922671394799046,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 1876.3655555555554,
            "unit": "mg"
          },
          {
            "daily": 43.50814814814815,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 7.8314666666666675,
            "unit": "mg"
          },
          {
            "daily": 32.725,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 3.5997500000000002,
            "unit": "mg"
          },
          {
            "daily": 69.19388888888888,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 484.3572222222222,
            "unit": "mg"
          },
          {
            "daily": 19.689444444444444,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 177.205,
            "unit": "\u00b5g"
          },
          {
            "daily": 288.37209876543216,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 259.53488888888893,
            "unit": "mg"
          },
          {
            "daily": 55.55532407407408,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.666663888888889,
            "unit": "mg"
          },
          {
            "daily": 53.076666666666654,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.6899966666666666,
            "unit": "mg"
          },
          {
            "daily": 40.09373958333333,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 6.414998333333333,
            "unit": "mg"
          },
          {
            "daily": 80.36893162393162,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 1.044796111111111,
            "unit": "mg"
          },
          {
            "daily": 94.47583333333334,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 377.90333333333336,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 327.86333333333334,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 29.52,
            "unit": "\u00b5g"
          },
          {
            "daily": 11.666666666666668,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.28,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.7000000000000001,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.10500000000000001,
            "unit": "\u00b5g"
          },
          {
            "daily": 19.998148148148154,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 2.9997222222222226,
            "unit": "mg"
          },
          {
            "daily": 84.78171296296296,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 101.73805555555555,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 756.6196,
            "unit": "g"
          }
        ],
        "dishType": [
          "starter"
        ],
        "healthLabels": [
          "Sugar-Conscious",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Sulfite-Free"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/b68/b68daac418c6aaeaece8cbb3d284b00a.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=f1f2c794a1efe0c787f1b9b6032fe47c3e6053ed107ed6adb7358f8c57361b10",
        "images": {
          "LARGE": {
            "height": 600,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/b68/b68daac418c6aaeaece8cbb3d284b00a-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a8f4fbaae17080b16c9d35ba696d644ca9b9f207a29f1deec953c55249a0314d",
            "width": 600
          },
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/b68/b68daac418c6aaeaece8cbb3d284b00a.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=f1f2c794a1efe0c787f1b9b6032fe47c3e6053ed107ed6adb7358f8c57361b10",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/b68/b68daac418c6aaeaece8cbb3d284b00a-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=11846cbe7bcd8c483442525954dc98e60fd3c2e0bbd9b9ee0bb2bc08cee3e2a2",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/b68/b68daac418c6aaeaece8cbb3d284b00a-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=2609ed7a58f01a48064dbe4ce390ef1b2402f267189d9732bd45586d72c98422",
            "width": 100
          }
        },
        "ingredientLines": [
          "1 head of cauliflower",
          "1/2 to 3/4 bag of shredded cheddar",
          "1 can of condensed cream of chicken soup",
          "1 1/2 teaspoons of mild curry powder",
          "1/3 cup mayonnaise paprika breadcrumbs"
        ],
        "ingredients": [
          {
            "food": "cauliflower",
            "foodCategory": "vegetables",
            "foodId": "food_buqfaxubzh6hi5asev8a5aj9sr71",
            "image": "https://www.edamam.com/food-img/ca2/ca217d31067dffd35ce1215e7f336bd8.jpg",
            "measure": "head",
            "quantity": 1.0,
            "text": "1 head of cauliflower",
            "weight": 537.7777777777777
          },
          {
            "food": "cheddar",
            "foodCategory": "Cheese",
            "foodId": "food_bhppgmha1u27voagb8eptbp9g376",
            "image": "https://www.edamam.com/food-img/bcd/bcd94dde1fcde1475b5bf0540f821c5d.jpg",
            "measure": "<unit>",
            "quantity": 0.625,
            "text": "1/2 to 3/4 bag of shredded cheddar",
            "weight": 17.5
          },
          {
            "food": "can of condensed cream of chicken soup",
            "foodCategory": "canned soup",
            "foodId": "food_bss83roarr59m6ahbwlfnb138xbk",
            "image": "https://www.edamam.com/food-img/525/525584dcb2f4c027b7d0063e4204ba33.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 can of condensed cream of chicken soup",
            "weight": 305.0
          },
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "teaspoon",
            "quantity": 1.5,
            "text": "1 1/2 teaspoons of mild curry powder",
            "weight": 3.0
          },
          {
            "food": "breadcrumbs",
            "foodCategory": "bread, rolls and tortillas",
            "foodId": "food_ata1dxza443wfda7jb4e5b3zwt9p",
            "image": "https://www.edamam.com/food-img/349/349f852497885b9d9c0b195ad0d0db8f.jpg",
            "measure": "cup",
            "quantity": 0.3333333333333333,
            "text": "1/3 cup mayonnaise paprika breadcrumbs",
            "weight": 36.0
          }
        ],
        "label": "Cauliflower Curry",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/cauliflower-curry-3886b0a75bb05ac5beec1106fb318a4a/curry",
        "source": "Big Girls Small Kitchen",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 36.07661111111111,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 25.462001851851852,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 14.083333333333334,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 31.597222222222218,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 48.73440555555556,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 42.078581196581204,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 43.50814814814815,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 55.886222222222216,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 94.47583333333334,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 39.922671394799046,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 28.743253968253967,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 111.67555555555558,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 40.09373958333333,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 69.19388888888888,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 54.05206666666666,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 53.076666666666654,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 55.55532407407408,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 19.998148148148154,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 19.689444444444444,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 11.666666666666668,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 80.36893162393162,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 288.37209876543216,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.7000000000000001,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 84.78171296296296,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 32.725,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 360.7661111111111,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 76.38600555555556,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 62.41445,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 42.25,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 631.9444444444443,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 8.560284444444445,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 4.4929161111111116,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 9.746881111111112,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 27.351077777777782,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.20632500000000004,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 7.8314666666666675,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 13.971555555555554,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 29.52,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 377.90333333333336,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 327.86333333333334,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 1876.3655555555554,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 120.72166666666666,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 2680.2133333333336,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 6.414998333333333,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 484.3572222222222,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 27.02603333333333,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.6899966666666666,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 14.282355555555554,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.666663888888889,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 2.9997222222222226,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 177.205,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.28,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 1.044796111111111,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 259.53488888888893,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.10500000000000001,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 101.73805555555555,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 756.6196,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 3.5997500000000002,
            "unit": "mg"
          }
        },
        "totalTime": 0.0,
        "totalWeight": 899.2777777777777,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_3886b0a75bb05ac5beec1106fb318a4a",
        "url": "http://www.biggirlssmallkitchen.com/2009/10/potluck-parties-mag-club-without.html",
        "yield": 4.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/34a4410adb1f92ac4b480c8595bf97fa?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 5516.404981292365,
        "cautions": [
          "Tree-Nuts",
          "Shellfish",
          "Sulfites",
          "FODMAP"
        ],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [
          "Low-Carb"
        ],
        "digest": [
          {
            "daily": 597.1179160245151,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 838.9468095790978,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 167.78936191581957,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 1.587573295,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 147.6434874644499,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 67.19223230235053,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 388.12664541593483,
            "unit": "g"
          },
          {
            "daily": 31.813344132840186,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 77.02355739829174,
                "unit": "g"
              },
              {
                "daily": 73.66590000091524,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 18.41647500022881,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 18.798645000916423,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 17.399175000882508,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 95.44003239852056,
            "unit": "g"
          },
          {
            "daily": 834.1299475196898,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 417.0649737598449,
            "unit": "g"
          },
          {
            "daily": 839.1458845,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 2517.4376535,
            "unit": "mg"
          },
          {
            "daily": 111.76289942231459,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 2682.30958613555,
            "unit": "mg"
          },
          {
            "daily": 50.68348517775629,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 506.8348517775629,
            "unit": "mg"
          },
          {
            "daily": 156.18537498266025,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 655.978574927173,
            "unit": "mg"
          },
          {
            "daily": 119.14783982462333,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 5599.948471757297,
            "unit": "mg"
          },
          {
            "daily": 169.17300941022575,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 30.451141693840636,
            "unit": "mg"
          },
          {
            "daily": 288.01975907294184,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 31.6821734980236,
            "unit": "mg"
          },
          {
            "daily": 480.0740237573784,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 3360.518166301649,
            "unit": "mg"
          },
          {
            "daily": 22.754285166669845,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 204.78856650002862,
            "unit": "\u00b5g"
          },
          {
            "daily": 6.276300819457108,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 5.648670737511398,
            "unit": "mg"
          },
          {
            "daily": 120.95066085215187,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 1.4514079302258225,
            "unit": "mg"
          },
          {
            "daily": 187.78476580781597,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 2.4412019555016076,
            "unit": "mg"
          },
          {
            "daily": 836.222337136355,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 133.7955739418168,
            "unit": "mg"
          },
          {
            "daily": 941.4479768194705,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 12.238823698653116,
            "unit": "mg"
          },
          {
            "daily": 63.296036206392635,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 253.18414482557054,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 253.18414482557054,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 238.0460260417884,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 5.713104625002922,
            "unit": "\u00b5g"
          },
          {
            "daily": 15.119745666666669,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 2.2679618500000003,
            "unit": "\u00b5g"
          },
          {
            "daily": 149.5379722673836,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 22.430695840107536,
            "unit": "mg"
          },
          {
            "daily": 97.98254191702101,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 117.57905030042521,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 1881.1339808646537,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Dairy-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Alcohol-Free",
          "No oil added",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/4ff/4ffbcb1bab438af2c083c3949badafaa.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=bbe99f53192c3da0c088d1e850e67be6ac6527fc06ebd786bd58fa48891ed108",
        "images": {
          "LARGE": {
            "height": 600,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/4ff/4ffbcb1bab438af2c083c3949badafaa-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=eb95495c59d879a6da92cc9359fddcfd56de872c862e127146947c3be198c173",
            "width": 600
          },
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/4ff/4ffbcb1bab438af2c083c3949badafaa.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=bbe99f53192c3da0c088d1e850e67be6ac6527fc06ebd786bd58fa48891ed108",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/4ff/4ffbcb1bab438af2c083c3949badafaa-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=bd8399f5928b10f98c20e466de97b7ea02462f39184613618ec6d51b0ffec30c",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/4ff/4ffbcb1bab438af2c083c3949badafaa-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=5ac098652aa7004c804f4fbd72c1e41f44bc513cac9007abfd78337f5d093a0d",
            "width": 100
          }
        },
        "ingredientLines": [
          "5 lbs Chicken Wings, tips trimmed, wings cut into 2 pieces",
          "1/2 c Flour",
          "1/4 c Curry Powder",
          "14 oz Coconut Milk",
          "3 T Curry Powder",
          "3 T Honey",
          "1 1/2 T Fish Sauce",
          "1 1/2 T Chili Garlic Sauce"
        ],
        "ingredients": [
          {
            "food": "Chicken Wings",
            "foodCategory": "Poultry",
            "foodId": "food_aftnyj9ap60fc6av2a9nfbju90c1",
            "image": "https://www.edamam.com/food-img/f92/f928682fc890edded472c5d8baeffed5.jpg",
            "measure": "pound",
            "quantity": 5.0,
            "text": "5 lbs Chicken Wings, tips trimmed, wings cut into 2 pieces",
            "weight": 2267.96185
          },
          {
            "food": "Flour",
            "foodCategory": "grains",
            "foodId": "food_ahebfs0a985an4aubqaebbipra58",
            "image": "https://www.edamam.com/food-img/b4c/b4c739e76a6f2172b7ad49d0aa41d5aa.jpg",
            "measure": "cup",
            "quantity": 0.5,
            "text": "1/2 c Flour",
            "weight": 62.5
          },
          {
            "food": "Curry Powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "cup",
            "quantity": 0.25,
            "text": "1/4 c Curry Powder",
            "weight": 25.200000000426055
          },
          {
            "food": "Coconut Milk",
            "foodCategory": "non-dairy beverages",
            "foodId": "food_by1k6v2adj7drhbq9w1rpbpen9ms",
            "image": "https://www.edamam.com/food-img/671/671f7528eadb1b01efb53243d0ef0f80.JPG",
            "measure": "ounce",
            "quantity": 14.0,
            "text": "14 oz Coconut Milk",
            "weight": 396.89332375000004
          },
          {
            "food": "Curry Powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "teaspoon",
            "quantity": 3.0,
            "text": "3 T Curry Powder",
            "weight": 6.0
          },
          {
            "food": "Honey",
            "foodCategory": null,
            "foodId": "food_bn6aoj9atkqx8fbkli859bbbxx62",
            "image": "https://www.edamam.com/food-img/198/198c7b25c23b4235b4cc33818c7b335f.jpg",
            "measure": "teaspoon",
            "quantity": 3.0,
            "text": "3 T Honey",
            "weight": 21.187500001074653
          },
          {
            "food": "Fish Sauce",
            "foodCategory": "canned soup",
            "foodId": "food_ahlu6u3ab8bu1wap7cbqua3s1quk",
            "image": "https://www.edamam.com/food-img/7b5/7b58b769d8bf7b79acf12a76b79ea9bc.jpg",
            "measure": "teaspoon",
            "quantity": 1.5,
            "text": "1 1/2 T Fish Sauce",
            "weight": 9.000000000608653
          },
          {
            "food": "Garlic",
            "foodCategory": "vegetables",
            "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
            "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg",
            "measure": "teaspoon",
            "quantity": 1.5,
            "text": "1 1/2 T Chili Garlic Sauce",
            "weight": 4.199999999999999
          }
        ],
        "label": "Curry Chicken Wings",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/curry-chicken-wings-34a4410adb1f92ac4b480c8595bf97fa/curry",
        "source": "White On Rice Couple",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 50.68348517775629,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 31.813344132840186,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 839.1458845,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 275.8202490646183,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 838.9468095790978,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 597.1179160245151,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 169.17300941022575,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 73.66590000091524,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 63.296036206392635,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 119.14783982462333,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 156.18537498266025,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 111.76289942231459,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 836.222337136355,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 480.0740237573784,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 834.1299475196898,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 187.78476580781597,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 120.95066085215187,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 149.5379722673836,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 22.754285166669845,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 238.0460260417884,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 941.4479768194705,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 6.276300819457108,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 15.119745666666669,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 97.98254191702101,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 288.01975907294184,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 506.8348517775629,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 95.44003239852056,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 77.02355739829174,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 2517.4376535,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 5516.404981292365,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 147.6434874644499,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 67.19223230235053,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 167.78936191581957,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 388.12664541593483,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 1.587573295,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 30.451141693840636,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 18.41647500022881,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 253.18414482557054,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 253.18414482557054,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 5599.948471757297,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 655.978574927173,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 2682.30958613555,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 133.7955739418168,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 3360.518166301649,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 417.0649737598449,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 2.4412019555016076,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 18.798645000916423,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 17.399175000882508,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 1.4514079302258225,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 22.430695840107536,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 204.78856650002862,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 5.713104625002922,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 12.238823698653116,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 5.648670737511398,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 2.2679618500000003,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 117.57905030042521,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 1881.1339808646537,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 31.6821734980236,
            "unit": "mg"
          }
        },
        "totalTime": 0.0,
        "totalWeight": 2792.942673752109,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_34a4410adb1f92ac4b480c8595bf97fa",
        "url": "http://whiteonricecouple.com/recipes/curry-chicken-wings/",
        "yield": 4.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/b639fcf8190eb6363de36a5cc134fc0c?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 59.7175,
        "cautions": [],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [
          "Balanced",
          "Low-Sodium"
        ],
        "digest": [
          {
            "daily": 3.372076923076923,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 1.2888549999999999,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 0.257771,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 1.3833975,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 0.391782,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 2.19185,
            "unit": "g"
          },
          {
            "daily": 3.7320616666666666,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 4.967735,
                "unit": "g"
              },
              {
                "daily": 24.913800000000002,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 6.2284500000000005,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 2.4341500000000003,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 2.0958,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 11.196185,
            "unit": "g"
          },
          {
            "daily": 4.32699,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 2.163495,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 0.0,
            "unit": "mg"
          },
          {
            "daily": 1.75864425,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 42.207462,
            "unit": "mg"
          },
          {
            "daily": 8.921079668940607,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 89.21079668940607,
            "unit": "mg"
          },
          {
            "daily": 10.316272784617125,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 43.32834569539193,
            "unit": "mg"
          },
          {
            "daily": 4.434814160917774,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 208.43626556313535,
            "unit": "mg"
          },
          {
            "daily": 21.44846710821852,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 3.8607240794793336,
            "unit": "mg"
          },
          {
            "daily": 6.243359723083564,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 0.686769569539192,
            "unit": "mg"
          },
          {
            "daily": 8.028142857142859,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 56.197,
            "unit": "mg"
          },
          {
            "daily": 0.20572222222222222,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 1.8515000000000001,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.8858888888888887,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 0.7972999999999999,
            "unit": "mg"
          },
          {
            "daily": 3.009583333333333,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.036114999999999994,
            "unit": "mg"
          },
          {
            "daily": 2.828153846153846,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.036766,
            "unit": "mg"
          },
          {
            "daily": 3.7762656249999997,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 0.6042025,
            "unit": "mg"
          },
          {
            "daily": 2.540192307692308,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 0.0330225,
            "unit": "mg"
          },
          {
            "daily": 1.2926250000000001,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 5.1705000000000005,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 5.1705000000000005,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 14.028066666666668,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 2.10421,
            "unit": "mg"
          },
          {
            "daily": 8.737875,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 10.48545,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 1.472659139078384,
            "unit": "g"
          }
        ],
        "dishType": [
          "condiments and sauces"
        ],
        "healthLabels": [
          "Low Potassium",
          "Kidney-Friendly",
          "Keto-Friendly",
          "Vegan",
          "Vegetarian",
          "Pescatarian",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "No oil added",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/123/123598e20fbcb93ee690fb4236f05d5a.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=68d64b71e4d09e2777f7b6ea4c58d0c954520a87baf2eb4376f4ea3bc6610755",
        "images": {
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/123/123598e20fbcb93ee690fb4236f05d5a.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=68d64b71e4d09e2777f7b6ea4c58d0c954520a87baf2eb4376f4ea3bc6610755",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/123/123598e20fbcb93ee690fb4236f05d5a-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=6d3b967facbfba6e9b0b9d42d271d93caa54ed09af3c1fe51540dcc397ab9fca",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/123/123598e20fbcb93ee690fb4236f05d5a-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=bdd04408cd5ed9f436cd44347036ce1e6ff353934acee73cdcf95ca71f5ca096",
            "width": 100
          }
        },
        "ingredientLines": [
          "4 teaspoons curry powder",
          "1 1/2 teaspoons ground coriander",
          "1 1/2 teaspoons coarse salt",
          "1 teaspoon ground ginger",
          "1 teaspoon ground cumin",
          "1/2 teaspoon ground pepper",
          "1/2 teaspoon sugar"
        ],
        "ingredients": [
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "teaspoon",
            "quantity": 4.0,
            "text": "4 teaspoons curry powder",
            "weight": 8.0
          },
          {
            "food": "coriander",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_afpcy6rb44nx6gbfff63ga2cqksw",
            "image": "https://www.edamam.com/food-img/a90/a901cee0b9028841d258f5d07b5924e7.jpg",
            "measure": "teaspoon",
            "quantity": 1.5,
            "text": "1 1/2 teaspoons ground coriander",
            "weight": 2.7
          },
          {
            "food": "coarse salt",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_a1vgrj1bs8rd1majvmd9ubz8ttkg",
            "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg",
            "measure": "teaspoon",
            "quantity": 1.5,
            "text": "1 1/2 teaspoons coarse salt",
            "weight": 7.2812500003693135
          },
          {
            "food": "ground ginger",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_a8l1yfna3fgp3ha4a5b5labyetgz",
            "image": "https://www.edamam.com/food-img/ee0/ee08c937de5c45a36bd0ad1eafc67496.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 teaspoon ground ginger",
            "weight": 1.8
          },
          {
            "food": "cumin",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_a8jjbx4biqndasapojdb5by3e92e",
            "image": "https://www.edamam.com/food-img/07e/07e2a4eb77ce46591033846504817d35.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 teaspoon ground cumin",
            "weight": 2.1
          },
          {
            "food": "ground pepper",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_b6ywzluaaxv02wad7s1r9ag4py89",
            "image": "https://www.edamam.com/food-img/c6e/c6e5c3bd8d3bc15175d9766971a4d1b2.jpg",
            "measure": "teaspoon",
            "quantity": 0.5,
            "text": "1/2 teaspoon ground pepper",
            "weight": 1.45
          },
          {
            "food": "sugar",
            "foodCategory": "sugars",
            "foodId": "food_axi2ijobrk819yb0adceobnhm1c2",
            "image": "https://www.edamam.com/food-img/ecb/ecb3f5aaed96d0188c21b8369be07765.jpg",
            "measure": "teaspoon",
            "quantity": 0.5,
            "text": "1/2 teaspoon sugar",
            "weight": 2.1
          }
        ],
        "label": "Curry Rub",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/curry-rub-b639fcf8190eb6363de36a5cc134fc0c/curry",
        "source": "Martha Stewart",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 8.921079668940607,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 3.7320616666666666,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 2.985875,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 1.2888549999999999,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 3.372076923076923,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 21.44846710821852,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 24.913800000000002,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 1.2926250000000001,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 4.434814160917774,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 10.316272784617125,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 1.75864425,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 3.7762656249999997,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 8.028142857142859,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 4.32699,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 2.828153846153846,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 3.009583333333333,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 14.028066666666668,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 0.20572222222222222,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 2.540192307692308,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 0.8858888888888887,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 8.737875,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 6.243359723083564,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 89.21079668940607,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 11.196185,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 4.967735,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 59.7175,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 1.3833975,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 0.391782,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 0.257771,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 2.19185,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 3.8607240794793336,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 6.2284500000000005,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 5.1705000000000005,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 5.1705000000000005,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 208.43626556313535,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 43.32834569539193,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 42.207462,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 0.6042025,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 56.197,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 2.163495,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.036766,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 2.4341500000000003,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 2.0958,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.036114999999999994,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 2.10421,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 1.8515000000000001,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 0.0330225,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 0.7972999999999999,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 10.48545,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 1.472659139078384,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 0.686769569539192,
            "unit": "mg"
          }
        },
        "totalTime": 0.0,
        "totalWeight": 18.23456953919191,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_b639fcf8190eb6363de36a5cc134fc0c",
        "url": "https://www.marthastewart.com/337591/curry-rub",
        "yield": 10.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/94996060ba29ed1cd02c150f1b70d344?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 419.085000001089,
        "cautions": [
          "Soy",
          "Sulfites"
        ],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [
          "Low-Carb",
          "Low-Sodium"
        ],
        "digest": [
          {
            "daily": 60.033692307692306,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 26.998550000000005,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 5.399710000000001,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 9.252865,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 22.644740000000002,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 39.0219,
            "unit": "g"
          },
          {
            "daily": 5.263733333431723,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 13.649075000294456,
                "unit": "g"
              },
              {
                "daily": 8.568500000002865,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 2.1421250000007164,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 10.761125000294168,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 5.799725000294168,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 15.791200000295172,
            "unit": "g"
          },
          {
            "daily": 3.264575000002149,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 1.6322875000010746,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 0.0,
            "unit": "mg"
          },
          {
            "daily": 35.3740625000006,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 848.9775000000144,
            "unit": "mg"
          },
          {
            "daily": 2.1423750000021493,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 21.423750000021492,
            "unit": "mg"
          },
          {
            "daily": 2.462202380954087,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 10.341250000007165,
            "unit": "mg"
          },
          {
            "daily": 2.7203723404294955,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 127.85750000018628,
            "unit": "mg"
          },
          {
            "daily": 4.40923611111947,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 0.7936625000015046,
            "unit": "mg"
          },
          {
            "daily": 1.8503409090980734,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 0.20353750000078807,
            "unit": "mg"
          },
          {
            "daily": 2.137500000002047,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 14.962500000014328,
            "unit": "mg"
          },
          {
            "daily": 0.0044444444444444444,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 0.04,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.07034722222421232,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 0.06331250000179109,
            "unit": "mg"
          },
          {
            "daily": 0.5866666666666667,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.007039999999999999,
            "unit": "mg"
          },
          {
            "daily": 0.821826923087394,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.010683750000136123,
            "unit": "mg"
          },
          {
            "daily": 0.8684101562527089,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 0.13894562500043342,
            "unit": "mg"
          },
          {
            "daily": 0.45346153846815174,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 0.005895000000085972,
            "unit": "mg"
          },
          {
            "daily": 0.5953125000017911,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 2.3812500000071646,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 2.3812500000071646,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 56.24166666666666,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 8.43625,
            "unit": "mg"
          },
          {
            "daily": 27.100416666666664,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 32.5205,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 66.23968750006127,
            "unit": "g"
          }
        ],
        "dishType": [
          "starter"
        ],
        "healthLabels": [
          "Low Potassium",
          "Kidney-Friendly",
          "Keto-Friendly",
          "Vegetarian",
          "Pescatarian",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/4eb/4eb6605a116f1ff98bd8cf22237e24e0.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=dc644af2daefe16ddf69246f86ec7f52ef330d68a4c76fdd05939e0f2ed03aa7",
        "images": {
          "LARGE": {
            "height": 600,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/4eb/4eb6605a116f1ff98bd8cf22237e24e0-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=5e819276fa96e40ef4fd172681fe10a8301e0dc56c3f4e54e6b909ebd00ada05",
            "width": 600
          },
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/4eb/4eb6605a116f1ff98bd8cf22237e24e0.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=dc644af2daefe16ddf69246f86ec7f52ef330d68a4c76fdd05939e0f2ed03aa7",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/4eb/4eb6605a116f1ff98bd8cf22237e24e0-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=8fe7b90130a0d621e933009176497712d4d936f7c1aaddf129067d8e6122f9f1",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/4eb/4eb6605a116f1ff98bd8cf22237e24e0-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=9534b97fbd34dc4cc482b34b3f61717967e9750b203cf85486f1e2172fc8a2ba",
            "width": 100
          }
        },
        "ingredientLines": [
          "2 teaspoons curry powder",
          "\u00bd cup reduced-fat mayonnaise",
          "1 teaspoon honey"
        ],
        "ingredients": [
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "teaspoon",
            "quantity": 2.0,
            "text": "2 teaspoons curry powder",
            "weight": 4.0
          },
          {
            "food": "reduced-fat mayonnaise",
            "foodCategory": "condiments and sauces",
            "foodId": "food_bkiqrl6auomqe8aj2ka7ebh36m91",
            "image": "https://www.edamam.com/food-img/58c/58c73d18780bc20e434dfffa8907c20f.jpg",
            "measure": "cup",
            "quantity": 0.5,
            "text": "\u00bd cup reduced-fat mayonnaise",
            "weight": 115.5
          },
          {
            "food": "honey",
            "foodCategory": null,
            "foodId": "food_bn6aoj9atkqx8fbkli859bbbxx62",
            "image": "https://www.edamam.com/food-img/198/198c7b25c23b4235b4cc33818c7b335f.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 teaspoon honey",
            "weight": 7.0625000003582175
          }
        ],
        "label": "Curry Mayonnaise",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/curry-mayonnaise-94996060ba29ed1cd02c150f1b70d344/curry",
        "source": "EatingWell",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 2.1423750000021493,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 5.263733333431723,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 20.95425000005445,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 26.998550000000005,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 60.033692307692306,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 4.40923611111947,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 8.568500000002865,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 0.5953125000017911,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 2.7203723404294955,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 2.462202380954087,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 35.3740625000006,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 0.8684101562527089,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 2.137500000002047,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 3.264575000002149,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.821826923087394,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.5866666666666667,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 56.24166666666666,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 0.0044444444444444444,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 0.45346153846815174,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 0.07034722222421232,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 27.100416666666664,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 1.8503409090980734,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 21.423750000021492,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 15.791200000295172,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 13.649075000294456,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 419.085000001089,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 9.252865,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 22.644740000000002,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 5.399710000000001,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 39.0219,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 0.7936625000015046,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 2.1421250000007164,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 2.3812500000071646,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 2.3812500000071646,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 127.85750000018628,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 10.341250000007165,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 848.9775000000144,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 0.13894562500043342,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 14.962500000014328,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 1.6322875000010746,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.010683750000136123,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 10.761125000294168,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 5.799725000294168,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.007039999999999999,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 8.43625,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 0.04,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 0.005895000000085972,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 0.06331250000179109,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 32.5205,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 66.23968750006127,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 0.20353750000078807,
            "unit": "mg"
          }
        },
        "totalTime": 10.0,
        "totalWeight": 126.56250000035821,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_94996060ba29ed1cd02c150f1b70d344",
        "url": "http://www.eatingwell.com/recipe/248143/curry-mayonnaise/",
        "yield": 8.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/eb29b67a84c4a1df35a9009b53bd5b31?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 3502.9569583337757,
        "cautions": [
          "Sulfites"
        ],
        "cuisineType": [
          "indian",
          "south east asian"
        ],
        "dietLabels": [],
        "digest": [
          {
            "daily": 309.3331480769237,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 258.12081104166685,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 51.624162208333374,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.27625,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 105.38628987500007,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 30.745362750000194,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 201.06654625000039,
            "unit": "g"
          },
          {
            "daily": 110.59678138892686,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 296.76283583344434,
                "unit": "g"
              },
              {
                "daily": 140.11003333334506,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 35.027508333336264,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 27.06628583344427,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 8.3832,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 331.7903441667806,
            "unit": "g"
          },
          {
            "daily": 199.9481033333345,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 99.97405166666726,
            "unit": "g"
          },
          {
            "daily": 106.16666666666667,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 318.5,
            "unit": "mg"
          },
          {
            "daily": 151.4537483958617,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 3634.8899615006812,
            "unit": "mg"
          },
          {
            "daily": 39.273878596444106,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 392.73878596444104,
            "unit": "mg"
          },
          {
            "daily": 82.2988487364217,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 345.65516469297114,
            "unit": "mg"
          },
          {
            "daily": 90.80754753639238,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 4267.9547342104415,
            "unit": "mg"
          },
          {
            "daily": 143.2267718445086,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 25.78081893201155,
            "unit": "mg"
          },
          {
            "daily": 88.41026714511861,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 9.725129385963047,
            "unit": "mg"
          },
          {
            "daily": 179.4298928571454,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 1256.0092500000178,
            "unit": "mg"
          },
          {
            "daily": 11.523824074074724,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 103.7144166666725,
            "unit": "\u00b5g"
          },
          {
            "daily": 164.78412962963617,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 148.30571666667254,
            "unit": "mg"
          },
          {
            "daily": 198.89913541667033,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 2.386789625000044,
            "unit": "mg"
          },
          {
            "daily": 145.7367596153893,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 1.894577875000061,
            "unit": "mg"
          },
          {
            "daily": 241.22919270833515,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 38.596670833333626,
            "unit": "mg"
          },
          {
            "daily": 279.54253205128515,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 3.6340529166667075,
            "unit": "mg"
          },
          {
            "daily": 158.53542708333407,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 634.1417083333363,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 217.89170833333625,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 243.75,
            "unit": "\u00b5g"
          },
          {
            "daily": 83.95833333333334,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 2.015,
            "unit": "\u00b5g"
          },
          {
            "daily": 2.1666666666666665,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.325,
            "unit": "\u00b5g"
          },
          {
            "daily": 50.96838611112731,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 7.645257916669096,
            "unit": "mg"
          },
          {
            "daily": 82.75749305555898,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 99.30899166667076,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 916.3547983554366,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Sugar-Conscious",
          "Kidney-Friendly",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/dab/dab1884b66f1d3c7f469177289fb72cc.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e6b2183c807abe6745f3424862f421291a311e45ff83179d65b6f83d95d8b1af",
        "images": {
          "LARGE": {
            "height": 600,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/dab/dab1884b66f1d3c7f469177289fb72cc-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=7166d0808a4842d1c76bc5a8cd00c4dab764714ee738abe00a76a093c64b98be",
            "width": 600
          },
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/dab/dab1884b66f1d3c7f469177289fb72cc.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e6b2183c807abe6745f3424862f421291a311e45ff83179d65b6f83d95d8b1af",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/dab/dab1884b66f1d3c7f469177289fb72cc-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=0980561d3cb23c1db2a1e84f0448fa23ee07ce73c647e8c12a9a3e63336eb3b4",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/dab/dab1884b66f1d3c7f469177289fb72cc-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=5d001a5b17015641129cdc8efe874e9c950406298df3ac62678832b9764781bd",
            "width": 100
          }
        },
        "ingredientLines": [
          "375g ready rolled puff pastry",
          "325g chicken thigh fillet",
          "1 tablespoon worcestershire sauce",
          "3 potatoes",
          "1 large onion",
          "5 cloves garlic",
          "15 dried curry leaves",
          "3 tablespoons curry powder",
          "2 teaspoons sugar",
          "1 teaspoon cranberry sauce (optional)",
          "salt & pepper to taste"
        ],
        "ingredients": [
          {
            "food": "puff pastry",
            "foodCategory": "quick breads and pastries",
            "foodId": "food_bdy019nbzjeni3atliworbbgahrk",
            "image": "https://www.edamam.com/food-img/bc7/bc7dc9b99ce87d5a6dc136e30d6aadd1.jpg",
            "measure": "gram",
            "quantity": 375.0,
            "text": "375g ready rolled puff pastry",
            "weight": 375.0
          },
          {
            "food": "chicken thigh",
            "foodCategory": "Poultry",
            "foodId": "food_bsarl08be0gwarb34bpviafna9d4",
            "image": "https://www.edamam.com/food-img/007/00792642367e1f55de680762f85cfb3b.jpg",
            "measure": "gram",
            "quantity": 325.0,
            "text": "325g chicken thigh fillet",
            "weight": 325.0
          },
          {
            "food": "worcestershire sauce",
            "foodCategory": "canned soup",
            "foodId": "food_ahb8mscbejo58ubexo0itam1i74g",
            "image": "https://www.edamam.com/food-img/072/072b61dd1ad5bb641f05b14f716ba6d0.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoon worcestershire sauce",
            "weight": 17.0
          },
          {
            "food": "potatoes",
            "foodCategory": "vegetables",
            "foodId": "food_abiw5baauresjmb6xpap2bg3otzu",
            "image": "https://www.edamam.com/food-img/651/6512e82417bce15c2899630c1a2799df.jpg",
            "measure": "<unit>",
            "quantity": 3.0,
            "text": "3 potatoes",
            "weight": 639.0
          },
          {
            "food": "onion",
            "foodCategory": "vegetables",
            "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
            "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 large onion",
            "weight": 150.0
          },
          {
            "food": "garlic",
            "foodCategory": "vegetables",
            "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
            "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg",
            "measure": "clove",
            "quantity": 5.0,
            "text": "5 cloves garlic",
            "weight": 15.0
          },
          {
            "food": "curry leaves",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_asx39x4ayja4jab6ivj6zayvkblo",
            "image": "https://www.edamam.com/food-img/0f9/0f9f5f95df173e9ffaaff2977bef88f3.jpg",
            "measure": "<unit>",
            "quantity": 15.0,
            "text": "15 dried curry leaves",
            "weight": 9.0
          },
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "tablespoon",
            "quantity": 3.0,
            "text": "3 tablespoons curry powder",
            "weight": 18.9
          },
          {
            "food": "sugar",
            "foodCategory": "sugars",
            "foodId": "food_axi2ijobrk819yb0adceobnhm1c2",
            "image": "https://www.edamam.com/food-img/ecb/ecb3f5aaed96d0188c21b8369be07765.jpg",
            "measure": "teaspoon",
            "quantity": 2.0,
            "text": "2 teaspoons sugar",
            "weight": 8.4
          },
          {
            "food": "cranberry sauce",
            "foodCategory": "canned fruit",
            "foodId": "food_asvapqhatz4wejanlapyzbmov2k1",
            "image": "https://www.edamam.com/food-img/52c/52cd53c02e0d777330aa795c56230581.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 teaspoon cranberry sauce (optional)",
            "weight": 5.770833333626036
          },
          {
            "food": "salt",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
            "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg",
            "measure": null,
            "quantity": 0.0,
            "text": "salt & pepper to taste",
            "weight": 9.378425000001759
          }
        ],
        "label": "Malaysian Curry Puff",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/malaysian-curry-puff-eb29b67a84c4a1df35a9009b53bd5b31/curry",
        "source": "Food52",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 39.273878596444106,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 110.59678138892686,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 106.16666666666667,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 175.14784791668876,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 258.12081104166685,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 309.3331480769237,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 143.2267718445086,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 140.11003333334506,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 158.53542708333407,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 90.80754753639238,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 82.2988487364217,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 151.4537483958617,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 241.22919270833515,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 179.4298928571454,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 199.9481033333345,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 145.7367596153893,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 198.89913541667033,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 50.96838611112731,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 11.523824074074724,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 83.95833333333334,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 279.54253205128515,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 164.78412962963617,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 2.1666666666666665,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 82.75749305555898,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 88.41026714511861,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 392.73878596444104,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 331.7903441667806,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 296.76283583344434,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 318.5,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 3502.9569583337757,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 105.38628987500007,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 30.745362750000194,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 51.624162208333374,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 201.06654625000039,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.27625,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 25.78081893201155,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 35.027508333336264,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 243.75,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 634.1417083333363,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 217.89170833333625,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 4267.9547342104415,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 345.65516469297114,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 3634.8899615006812,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 38.596670833333626,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 1256.0092500000178,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 99.97405166666726,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 1.894577875000061,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 27.06628583344427,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 8.3832,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 2.386789625000044,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 7.645257916669096,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 103.7144166666725,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 2.015,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 3.6340529166667075,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 148.30571666667254,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.325,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 99.30899166667076,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 916.3547983554366,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 9.725129385963047,
            "unit": "mg"
          }
        },
        "totalTime": 0.0,
        "totalWeight": 1568.774802629859,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_eb29b67a84c4a1df35a9009b53bd5b31",
        "url": "https://food52.com/recipes/25062-malaysian-curry-puff",
        "yield": 20.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/d67920cf9dff811cfa122c3c8e98d753?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 1433.8551143125,
        "cautions": [
          "Sulfites"
        ],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [
          "Balanced",
          "High-Fiber"
        ],
        "digest": [
          {
            "daily": 78.64439033365385,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 28.070596923125002,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 5.614119384625001,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 24.201120185500002,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 11.1876466585625,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 51.118853716875,
            "unit": "g"
          },
          {
            "daily": 64.615875600625,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 137.28854240187502,
                "unit": "g"
              },
              {
                "daily": 226.2363376,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 56.5590844,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 34.214876319374994,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 193.847626801875,
            "unit": "g"
          },
          {
            "daily": 121.06168281874997,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 60.53084140937499,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 0.0,
            "unit": "mg"
          },
          {
            "daily": 87.28395027604165,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 2094.8148066249996,
            "unit": "mg"
          },
          {
            "daily": 40.39885621874999,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 403.98856218749995,
            "unit": "mg"
          },
          {
            "daily": 55.07768580357142,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 231.32628037499995,
            "unit": "mg"
          },
          {
            "daily": 23.801744130319147,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 1118.681974125,
            "unit": "mg"
          },
          {
            "daily": 55.641094017361105,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 10.015396923125,
            "unit": "mg"
          },
          {
            "daily": 50.4187260965909,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 5.546059870624999,
            "unit": "mg"
          },
          {
            "daily": 105.37040566964285,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 737.5928396874999,
            "unit": "mg"
          },
          {
            "daily": 0.949428548611111,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 8.544856937499999,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.9760952152777779,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 0.8784856937500001,
            "unit": "mg"
          },
          {
            "daily": 19.722594776041667,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.23667113731249997,
            "unit": "mg"
          },
          {
            "daily": 10.428681081730769,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.1355728540625,
            "unit": "mg"
          },
          {
            "daily": 8.2567498203125,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 1.32107997125,
            "unit": "mg"
          },
          {
            "daily": 76.21256959615384,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 0.99076340475,
            "unit": "mg"
          },
          {
            "daily": 102.61828324999999,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 410.47313299999996,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 410.47313299999996,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 49.003390079166664,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 7.350508511874999,
            "unit": "mg"
          },
          {
            "daily": 40.96876132291666,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 49.1625135875,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 567.7960548699999,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Kidney-Friendly",
          "Vegan",
          "Vegetarian",
          "Pescatarian",
          "Mediterranean",
          "DASH",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Sulfite-Free",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/5c5/5c5b3428f909ee81966e6cd9c78347e0.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=ff1dcd2e3c41435f35b7bcc7399c328cdb7a1d6e3dc931e8e17f3a0983159488",
        "images": {
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/5c5/5c5b3428f909ee81966e6cd9c78347e0.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=aebf8a4b82235772917f35966300c2b168bb1983f4762ba144771b50d20d3500",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/5c5/5c5b3428f909ee81966e6cd9c78347e0-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=5a749c0ad27c6ddc4cceb59b8b650d7d8bb458955870ca79e47b250a2ce6763b",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/5c5/5c5b3428f909ee81966e6cd9c78347e0-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c20d9844f5f819f5989d33179b669d548f7d2d60933a3410d81b8ee381341382",
            "width": 100
          }
        },
        "ingredientLines": [
          "2 (15-ounce) cans chickpeas, drained, rinsed, patted dry",
          "2 tablespoons olive oil",
          "2 teaspoons curry powder",
          "1 teaspoon kosher salt"
        ],
        "ingredients": [
          {
            "food": "cans chickpeas",
            "foodCategory": "plant-based protein",
            "foodId": "food_a63lcoybzox4krbbrj8eba9g8cz5",
            "image": "https://www.edamam.com/food-img/603/603965a58e6a5d127a522ffb44289d24.jpg",
            "measure": "ounce",
            "quantity": 30.0,
            "text": "2 (15-ounce) cans chickpeas, drained, rinsed, patted dry",
            "weight": 850.48569375
          },
          {
            "food": "olive oil",
            "foodCategory": "Oils",
            "foodId": "food_b1d1icuad3iktrbqby0hiagafaz7",
            "image": "https://www.edamam.com/food-img/4d6/4d651eaa8a353647746290c7a9b29d84.jpg",
            "measure": "tablespoon",
            "quantity": 2.0,
            "text": "2 tablespoons olive oil",
            "weight": 27.0
          },
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "teaspoon",
            "quantity": 2.0,
            "text": "2 teaspoons curry powder",
            "weight": 4.0
          },
          {
            "food": "kosher salt",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_a1vgrj1bs8rd1majvmd9ubz8ttkg",
            "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 teaspoon kosher salt",
            "weight": 4.854166666912875
          }
        ],
        "label": "Crispy Curry-Roasted Chickpeas",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/crispy-curry-roasted-chickpeas-d67920cf9dff811cfa122c3c8e98d753/curry",
        "source": "Epicurious",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 40.39885621874999,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 64.615875600625,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 71.692755715625,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 28.070596923125002,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 78.64439033365385,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 55.641094017361105,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 226.2363376,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 102.61828324999999,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 23.801744130319147,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 55.07768580357142,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 87.28395027604165,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 8.2567498203125,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 105.37040566964285,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 121.06168281874997,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 10.428681081730769,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 19.722594776041667,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 49.003390079166664,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 0.949428548611111,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 76.21256959615384,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 0.9760952152777779,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 40.96876132291666,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 50.4187260965909,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 403.98856218749995,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 193.847626801875,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 137.28854240187502,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 1433.8551143125,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 24.201120185500002,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 11.1876466585625,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 5.614119384625001,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 51.118853716875,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 10.015396923125,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 56.5590844,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 410.47313299999996,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 410.47313299999996,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 1118.681974125,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 231.32628037499995,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 2094.8148066249996,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 1.32107997125,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 737.5928396874999,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 60.53084140937499,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.1355728540625,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 34.214876319374994,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.23667113731249997,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 7.350508511874999,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 8.544856937499999,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 0.99076340475,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 0.8784856937500001,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 49.1625135875,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 567.7960548699999,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 5.546059870624999,
            "unit": "mg"
          }
        },
        "totalTime": 0.0,
        "totalWeight": 881.48569375,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_d67920cf9dff811cfa122c3c8e98d753",
        "url": "https://www.epicurious.com/recipes/food/views/crispy-curry-roasted-chickpeas-56389735",
        "yield": 6.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/83b0f8c85eff938e31eb4485a6947f79?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 1379.635808865,
        "cautions": [
          "Tree-Nuts",
          "Sulfites",
          "FODMAP"
        ],
        "cuisineType": [
          "mediterranean"
        ],
        "dietLabels": [
          "Balanced"
        ],
        "digest": [
          {
            "daily": 74.33288186841538,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 116.78085171384998,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 23.356170342769996,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 6.08332110732,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 8.553392350125,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 48.316373214470005,
            "unit": "g"
          },
          {
            "daily": 63.56265306378334,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 135.42248763167,
                "unit": "g"
              },
              {
                "daily": 221.06188623872004,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 55.26547155968001,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 32.37351564955,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 190.68795919135002,
            "unit": "g"
          },
          {
            "daily": 121.16201413798001,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 60.581007068990004,
            "unit": "g"
          },
          {
            "daily": 0.7359749094400001,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 2.20792472832,
            "unit": "mg"
          },
          {
            "daily": 91.08969570951251,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 2186.1526970283003,
            "unit": "mg"
          },
          {
            "daily": 43.80603761285557,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 438.0603761285556,
            "unit": "mg"
          },
          {
            "daily": 68.51429422080908,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 287.76003572739813,
            "unit": "mg"
          },
          {
            "daily": 30.526198829318833,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 1434.7313449779851,
            "unit": "mg"
          },
          {
            "daily": 80.7913906788855,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 14.54245032219939,
            "unit": "mg"
          },
          {
            "daily": 56.900039064998325,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 6.259004297149815,
            "unit": "mg"
          },
          {
            "daily": 119.46072174157143,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 836.225052191,
            "unit": "mg"
          },
          {
            "daily": 3.100377828688888,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 27.903400458199997,
            "unit": "\u00b5g"
          },
          {
            "daily": 6.9018500394444455,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 6.211665035500001,
            "unit": "mg"
          },
          {
            "daily": 23.68586937541667,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.284230432505,
            "unit": "mg"
          },
          {
            "daily": 12.312131901923077,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.160057714725,
            "unit": "mg"
          },
          {
            "daily": 15.610314206625,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 2.49765027306,
            "unit": "mg"
          },
          {
            "daily": 81.0713412046154,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 1.0539274356600001,
            "unit": "mg"
          },
          {
            "daily": 102.52162431160002,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 410.0864972464001,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 410.0864972464001,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.27014952,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.006483588479999998,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 28.892013448466667,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 4.33380201727,
            "unit": "mg"
          },
          {
            "daily": 29.460666087766672,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 35.352799305320005,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 630.9033871989998,
            "unit": "g"
          }
        ],
        "dishType": [
          "starter"
        ],
        "healthLabels": [
          "Sugar-Conscious",
          "Low Potassium",
          "Kidney-Friendly",
          "Vegan",
          "Vegetarian",
          "Pescatarian",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Sulfite-Free",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/e82/e822935fdbcdb9f19017c4cfd8f5bf06?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=0921c2b51e008ec07447232a1900c740d4247671a2ff6804e5d51805d2cfbcec",
        "images": {
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e82/e822935fdbcdb9f19017c4cfd8f5bf06?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=0921c2b51e008ec07447232a1900c740d4247671a2ff6804e5d51805d2cfbcec",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e82/e822935fdbcdb9f19017c4cfd8f5bf06-m?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=ae2bcaa3af1b67e33b4704c645c10e024b186fcbb40a5613ed01f51c5d33493b",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e82/e822935fdbcdb9f19017c4cfd8f5bf06-s?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b004507d69576ece7952d08b43d66405e87a0a2a3d265d7bd51968e3816fe3f5",
            "width": 100
          }
        },
        "ingredientLines": [
          "2 14-ounce cans chickpeas, drained and rinsed",
          "1/2 cup coconut milk",
          "1 1/2 tablespoons red curry paste",
          "1 tablespoon curry powder",
          "1 clove garlic",
          "1 teaspoon sea salt"
        ],
        "ingredients": [
          {
            "food": "cans chickpeas",
            "foodCategory": "plant-based protein",
            "foodId": "food_a63lcoybzox4krbbrj8eba9g8cz5",
            "image": "https://www.edamam.com/food-img/603/603965a58e6a5d127a522ffb44289d24.jpg",
            "measure": "ounce",
            "quantity": 28.0,
            "text": "2 14-ounce cans chickpeas, drained and rinsed",
            "weight": 793.7866475000001
          },
          {
            "food": "coconut milk",
            "foodCategory": "non-dairy beverages",
            "foodId": "food_by1k6v2adj7drhbq9w1rpbpen9ms",
            "image": "https://www.edamam.com/food-img/671/671f7528eadb1b01efb53243d0ef0f80.JPG",
            "measure": "cup",
            "quantity": 0.5,
            "text": "1/2 cup coconut milk",
            "weight": 113.0
          },
          {
            "food": "red curry paste",
            "foodCategory": "condiments and sauces",
            "foodId": "food_aojdol2are6zg7af2nincbe87jot",
            "image": "https://www.edamam.com/food-img/b6a/b6a9ebae5850f42eca0253827603ef9c.jpg",
            "measure": "tablespoon",
            "quantity": 1.5,
            "text": "1 1/2 tablespoons red curry paste",
            "weight": 24.0
          },
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoon curry powder",
            "weight": 6.3
          },
          {
            "food": "garlic",
            "foodCategory": "vegetables",
            "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
            "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg",
            "measure": "clove",
            "quantity": 1.0,
            "text": "1 clove garlic",
            "weight": 3.0
          },
          {
            "food": "sea salt",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_a1vgrj1bs8rd1majvmd9ubz8ttkg",
            "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 teaspoon sea salt",
            "weight": 4.854166666912875
          }
        ],
        "label": "Curry Hummus recipes",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/curry-hummus-recipes-83b0f8c85eff938e31eb4485a6947f79/curry",
        "source": "Pinch of Yum",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 43.80603761285557,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 63.56265306378334,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.7359749094400001,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 68.98179044324999,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 116.78085171384998,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 74.33288186841538,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 80.7913906788855,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 221.06188623872004,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 102.52162431160002,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 30.526198829318833,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 68.51429422080908,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 91.08969570951251,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 15.610314206625,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 119.46072174157143,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 121.16201413798001,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 12.312131901923077,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 23.68586937541667,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 28.892013448466667,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 3.100377828688888,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.27014952,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 81.0713412046154,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 6.9018500394444455,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 29.460666087766672,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 56.900039064998325,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 438.0603761285556,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 190.68795919135002,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 135.42248763167,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 2.20792472832,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 1379.635808865,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 6.08332110732,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 8.553392350125,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 23.356170342769996,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 48.316373214470005,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 14.54245032219939,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 55.26547155968001,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 410.0864972464001,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 410.0864972464001,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 1434.7313449779851,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 287.76003572739813,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 2186.1526970283003,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 2.49765027306,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 836.225052191,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 60.581007068990004,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.160057714725,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 32.37351564955,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.284230432505,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 4.33380201727,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 27.903400458199997,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.006483588479999998,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 1.0539274356600001,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 6.211665035500001,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 35.352799305320005,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 630.9033871989998,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 6.259004297149815,
            "unit": "mg"
          }
        },
        "totalTime": 10.0,
        "totalWeight": 940.327623799815,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_83b0f8c85eff938e31eb4485a6947f79",
        "url": "http://pinchofyum.com/curry-hummus",
        "yield": 12.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/19cd66589810a3793aa2ff57bd3d0c88?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 729.6515885865692,
        "cautions": [
          "Tree-Nuts"
        ],
        "cuisineType": [
          "mexican"
        ],
        "dietLabels": [],
        "digest": [
          {
            "daily": 68.3100095265644,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 184.26885778841364,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 36.85377155768273,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 2.8023596265072794,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 1.3524134646130546,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 44.40150619226686,
            "unit": "g"
          },
          {
            "daily": 27.544964750631863,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 60.41014259037861,
                "unit": "g"
              },
              {
                "daily": 88.89900664606792,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 22.22475166151698,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 31.62872123529356,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 2.0958,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 82.63489425189559,
            "unit": "g"
          },
          {
            "daily": 41.56302967379441,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 20.781514836897202,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 0.0,
            "unit": "mg"
          },
          {
            "daily": 83.90967113612413,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 2013.8321072669792,
            "unit": "mg"
          },
          {
            "daily": 37.05918780883592,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 370.59187808835924,
            "unit": "mg"
          },
          {
            "daily": 63.51979666058786,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 266.783145974469,
            "unit": "mg"
          },
          {
            "daily": 67.82713987601718,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 3187.8755741728073,
            "unit": "mg"
          },
          {
            "daily": 78.841052431201,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 14.19138943761618,
            "unit": "mg"
          },
          {
            "daily": 38.71748529322405,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 4.258923382254646,
            "unit": "mg"
          },
          {
            "daily": 90.6626419809338,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 634.6384938665366,
            "unit": "mg"
          },
          {
            "daily": 202.62371229815665,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 1823.61341068341,
            "unit": "\u00b5g"
          },
          {
            "daily": 429.2797614735547,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 386.35178532619926,
            "unit": "mg"
          },
          {
            "daily": 52.548484184841946,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.6305818102181033,
            "unit": "mg"
          },
          {
            "daily": 61.00919913229553,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.7931195887198419,
            "unit": "mg"
          },
          {
            "daily": 47.117413380247974,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 7.538786140839676,
            "unit": "mg"
          },
          {
            "daily": 132.4472529490416,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 1.721814288337541,
            "unit": "mg"
          },
          {
            "daily": 85.66476827561709,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 342.6590731024684,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 342.6590731024684,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.008668562500000001,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.0002080455,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0083082,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.00124623,
            "unit": "\u00b5g"
          },
          {
            "daily": 50.38595066406591,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 7.557892599609886,
            "unit": "mg"
          },
          {
            "daily": 194.45763456233956,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 233.3491614748075,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 1308.798106340299,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Vegan",
          "Vegetarian",
          "Pescatarian",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "No oil added",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/916/916871e9b23cb0e0de871621e6553f04.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=968ad89300ab4d2c2595d41b6f99607d05a5f07a146a3439a8eb1709df21e788",
        "images": {
          "LARGE": {
            "height": 600,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/916/916871e9b23cb0e0de871621e6553f04-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b25c081a59d2b24fbf55f0043facda242ff9a6bba5dfe9b7ddf1f923bd33d41d",
            "width": 600
          },
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/916/916871e9b23cb0e0de871621e6553f04.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=968ad89300ab4d2c2595d41b6f99607d05a5f07a146a3439a8eb1709df21e788",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/916/916871e9b23cb0e0de871621e6553f04-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=4098b1f82f40690559110209b34e0428668796426af1baa7cd586bfad8dce6e2",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/916/916871e9b23cb0e0de871621e6553f04-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d502a34bc9a275629cf665c091787b2dc6183267d9bfc47433702897586879f1",
            "width": 100
          }
        },
        "ingredientLines": [
          "150g broccoli",
          "150g cauliflower",
          "100g carrot",
          "100g long beans",
          "200g pumpkin",
          "1 onion",
          "Few cherry tomatoes",
          "1 tbsp garlic, chopped",
          "1\u00bd tbsp curry powder",
          "1\u00bd cup vegetable stock",
          "200ml coconut milk",
          "2 fresh chillies",
          "\u00be tsp salt and \u00bd tsp sugar, or to taste"
        ],
        "ingredients": [
          {
            "food": "broccoli",
            "foodCategory": "vegetables",
            "foodId": "food_aahw0jha9f8337ajbopx9aec6z7i",
            "image": "https://www.edamam.com/food-img/3e4/3e47317a3dd54dc911b9c44122285df1.jpg",
            "measure": "gram",
            "quantity": 150.0,
            "text": "150g broccoli",
            "weight": 150.0
          },
          {
            "food": "cauliflower",
            "foodCategory": "vegetables",
            "foodId": "food_buqfaxubzh6hi5asev8a5aj9sr71",
            "image": "https://www.edamam.com/food-img/ca2/ca217d31067dffd35ce1215e7f336bd8.jpg",
            "measure": "gram",
            "quantity": 150.0,
            "text": "150g cauliflower",
            "weight": 150.0
          },
          {
            "food": "carrot",
            "foodCategory": "vegetables",
            "foodId": "food_ai215e5b85pdh5ajd4aafa3w2zm8",
            "image": "https://www.edamam.com/food-img/121/121e33fce0bb9546ed7d060b6c114e29.jpg",
            "measure": "gram",
            "quantity": 100.0,
            "text": "100g carrot",
            "weight": 100.0
          },
          {
            "food": "beans",
            "foodCategory": "vegetables",
            "foodId": "food_aceucvpau4a8v6atkx5eabxyoqdn",
            "image": "https://www.edamam.com/food-img/891/89135f10639878a2360e6a33c9af3d91.jpg",
            "measure": "gram",
            "quantity": 100.0,
            "text": "100g long beans",
            "weight": 100.0
          },
          {
            "food": "pumpkin",
            "foodCategory": "vegetables",
            "foodId": "food_afk6bzsbbbg1j8ai1hi17bptbfq5",
            "image": "https://www.edamam.com/food-img/f5d/f5d6320e355878cbaef8ed891316946f.jpg",
            "measure": "gram",
            "quantity": 200.0,
            "text": "200g pumpkin",
            "weight": 200.0
          },
          {
            "food": "onion",
            "foodCategory": "vegetables",
            "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
            "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 onion",
            "weight": 125.0
          },
          {
            "food": "cherry tomatoes",
            "foodCategory": "vegetables",
            "foodId": "food_a30b0hpbvavginafe0tocbf6ymje",
            "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg",
            "measure": null,
            "quantity": 0.0,
            "text": "Few cherry tomatoes",
            "weight": 0.0
          },
          {
            "food": "garlic",
            "foodCategory": "vegetables",
            "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
            "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tbsp garlic, chopped",
            "weight": 8.499999999856291
          },
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "tablespoon",
            "quantity": 1.5,
            "text": "1\u00bd tbsp curry powder",
            "weight": 9.45
          },
          {
            "food": "vegetable stock",
            "foodCategory": "Vegan products",
            "foodId": "food_bb2qjrjamst0vmam39stubtkmrs4",
            "image": "https://www.edamam.com/food-img/e61/e6184a8681b772e5198ef0ca1919e1b7.jpg",
            "measure": "cup",
            "quantity": 1.5,
            "text": "1\u00bd cup vegetable stock",
            "weight": 340.5
          },
          {
            "food": "coconut milk",
            "foodCategory": "non-dairy beverages",
            "foodId": "food_by1k6v2adj7drhbq9w1rpbpen9ms",
            "image": "https://www.edamam.com/food-img/671/671f7528eadb1b01efb53243d0ef0f80.JPG",
            "measure": "milliliter",
            "quantity": 200.0,
            "text": "200ml coconut milk",
            "weight": 191.04922826541292
          },
          {
            "food": "chillies",
            "foodCategory": "vegetables",
            "foodId": "food_a6g98mqatzj7vca6ms3bnbzqxf3s",
            "image": "https://www.edamam.com/food-img/469/469213672957a242638e20c27e3e8acd.jpeg",
            "measure": "<unit>",
            "quantity": 2.0,
            "text": "2 fresh chillies",
            "weight": 90.0
          },
          {
            "food": "salt",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
            "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg",
            "measure": "teaspoon",
            "quantity": 0.75,
            "text": "\u00be tsp salt and \u00bd tsp sugar, or to taste",
            "weight": 4.5
          },
          {
            "food": "sugar",
            "foodCategory": "sugars",
            "foodId": "food_axi2ijobrk819yb0adceobnhm1c2",
            "image": "https://www.edamam.com/food-img/ecb/ecb3f5aaed96d0188c21b8369be07765.jpg",
            "measure": "teaspoon",
            "quantity": 0.5,
            "text": "\u00be tsp salt and \u00bd tsp sugar, or to taste",
            "weight": 2.1
          }
        ],
        "label": "Vegetable Curry",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/vegetable-curry-19cd66589810a3793aa2ff57bd3d0c88/curry",
        "source": "Honest Cooking",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 37.05918780883592,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 27.544964750631863,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 36.48257942932846,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 184.26885778841364,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 68.3100095265644,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 78.841052431201,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 88.89900664606792,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 85.66476827561709,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 67.82713987601718,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 63.51979666058786,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 83.90967113612413,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 47.117413380247974,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 90.6626419809338,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 41.56302967379441,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 61.00919913229553,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 52.548484184841946,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 50.38595066406591,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 202.62371229815665,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.008668562500000001,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 132.4472529490416,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 429.2797614735547,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0083082,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 194.45763456233956,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 38.71748529322405,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 370.59187808835924,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 82.63489425189559,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 60.41014259037861,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 729.6515885865692,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 2.8023596265072794,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 1.3524134646130546,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 36.85377155768273,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 44.40150619226686,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 14.19138943761618,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 22.22475166151698,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 342.6590731024684,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 342.6590731024684,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 3187.8755741728073,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 266.783145974469,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 2013.8321072669792,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 7.538786140839676,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 634.6384938665366,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 20.781514836897202,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.7931195887198419,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 31.62872123529356,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 2.0958,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.6305818102181033,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 7.557892599609886,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 1823.61341068341,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0002080455,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 1.721814288337541,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 386.35178532619926,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.00124623,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 233.3491614748075,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 1308.798106340299,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 4.258923382254646,
            "unit": "mg"
          }
        },
        "totalTime": 35.0,
        "totalWeight": 1471.0992282652692,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_19cd66589810a3793aa2ff57bd3d0c88",
        "url": "http://honestcooking.com/how-to-make-vegetable-curry/",
        "yield": 2.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/cb7810124de13e8a262788282abc2c45?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 1677.5902083332303,
        "cautions": [
          "Gluten",
          "Wheat",
          "Sulfites"
        ],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [
          "Low-Carb"
        ],
        "digest": [
          {
            "daily": 277.0562384615407,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 136.38522833333423,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 27.277045666666847,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 45.444324125001074,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 107.12527758333322,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 180.08655500000145,
            "unit": "g"
          },
          {
            "daily": 3.5612008333267924,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 6.718523333314143,
                "unit": "g"
              },
              {
                "daily": 15.86031666666494,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 3.965079166666235,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 2.2241362500116617,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 10.683602499980378,
            "unit": "g"
          },
          {
            "daily": 12.713598333321517,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 6.356799166660759,
            "unit": "g"
          },
          {
            "daily": 31.03,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 93.09,
            "unit": "mg"
          },
          {
            "daily": 166.18574479166847,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 3988.4578750000433,
            "unit": "mg"
          },
          {
            "daily": 9.896437499977866,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 98.96437499977867,
            "unit": "mg"
          },
          {
            "daily": 13.720833333335857,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 57.627500000010606,
            "unit": "mg"
          },
          {
            "daily": 8.30251773052091,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 390.21833333448274,
            "unit": "mg"
          },
          {
            "daily": 11.568819444439207,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 2.0823874999990575,
            "unit": "mg"
          },
          {
            "daily": 8.486344696959245,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 0.933497916665517,
            "unit": "mg"
          },
          {
            "daily": 20.318476190453644,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 142.2293333331755,
            "unit": "mg"
          },
          {
            "daily": 1.6707731481547643,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 15.036958333392878,
            "unit": "\u00b5g"
          },
          {
            "daily": 6.882888889036233,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 6.194600000132611,
            "unit": "mg"
          },
          {
            "daily": 4.954868055538918,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.059458416666467014,
            "unit": "mg"
          },
          {
            "daily": 12.0927884615472,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.1572062500001136,
            "unit": "mg"
          },
          {
            "daily": 8.630692708338222,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 1.3809108333341154,
            "unit": "mg"
          },
          {
            "daily": 15.608782051182532,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 0.2029141666653729,
            "unit": "mg"
          },
          {
            "daily": 3.395281250018933,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 13.581125000075732,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 13.581125000075732,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 5.625,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.135,
            "unit": "\u00b5g"
          },
          {
            "daily": 2.6,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.39,
            "unit": "\u00b5g"
          },
          {
            "daily": 10.959466666674691,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 1.6439200000012038,
            "unit": "mg"
          },
          {
            "daily": 5.719899305567975,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 6.86387916668157,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 75.62014583373077,
            "unit": "g"
          }
        ],
        "dishType": [
          "condiments and sauces"
        ],
        "healthLabels": [
          "Sugar-Conscious",
          "Keto-Friendly",
          "Vegetarian",
          "Pescatarian",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/42f/42f3f8a26f3870f128caa2927e5096d9?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b89da9d8407f95511acbbb04fd144f07d9ea26a136608b75412e57fbfeb34552",
        "images": {
          "LARGE": {
            "height": 600,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/42f/42f3f8a26f3870f128caa2927e5096d9-l?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=0f92fbc7bd43853238178b4c24301425c0ce6ef1636e0662e1e29fad0352c2af",
            "width": 600
          },
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/42f/42f3f8a26f3870f128caa2927e5096d9?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b89da9d8407f95511acbbb04fd144f07d9ea26a136608b75412e57fbfeb34552",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/42f/42f3f8a26f3870f128caa2927e5096d9-m?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=aaa74b179dfd67d6b3a24c7ceb83d3ceef31ffc34d32ed36f52233f9ee0a15d1",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/42f/42f3f8a26f3870f128caa2927e5096d9-s?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d3c3623516892bb8abea8d0a9113b8ae06bcbec1168d7e54e6c1f89c5f73a2c1",
            "width": 100
          }
        },
        "ingredientLines": [
          "1 tablespoon curry powder",
          "1 tablespoon minced garlic",
          "1 cup mayonnaise",
          "2 tablespoons milk",
          "1 teaspoon lemon juice",
          "3 tablespoons soy sauce",
          "1 teaspoon Chinese chile paste"
        ],
        "ingredients": [
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoon curry powder",
            "weight": 6.3
          },
          {
            "food": "garlic",
            "foodCategory": "vegetables",
            "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
            "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoon minced garlic",
            "weight": 8.499999999856291
          },
          {
            "food": "mayonnaise",
            "foodCategory": "condiments and sauces",
            "foodId": "food_bu8t61zaplle7dbrzk81dbygq0qj",
            "image": "https://www.edamam.com/food-img/577/577308a0422357885c94cc9b5f1f1862.jpg",
            "measure": "cup",
            "quantity": 1.0,
            "text": "1 cup mayonnaise",
            "weight": 231.0
          },
          {
            "food": "milk",
            "foodCategory": "Milk",
            "foodId": "food_b49rs1kaw0jktabzkg2vvanvvsis",
            "image": "https://www.edamam.com/food-img/7c9/7c9962acf83654a8d98ea6a2ade93735.jpg",
            "measure": "tablespoon",
            "quantity": 2.0,
            "text": "2 tablespoons milk",
            "weight": 30.0
          },
          {
            "food": "lemon juice",
            "foodCategory": "100% juice",
            "foodId": "food_bglm6vxahuauteb0n6ynfbg9eryu",
            "image": "https://www.edamam.com/food-img/e31/e310952d214e78a4cb8b73f30ceeaaf2.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 teaspoon lemon juice",
            "weight": 5.083333333591166
          },
          {
            "food": "soy sauce",
            "foodCategory": "plant-based protein",
            "foodId": "food_a5g9yevb1iactoaiimbvjbkrxueh",
            "image": "https://www.edamam.com/food-img/f56/f562e461eb0618f367f538b836c17b82.jpg",
            "measure": "tablespoon",
            "quantity": 3.0,
            "text": "3 tablespoons soy sauce",
            "weight": 48.0
          },
          {
            "food": "chile paste",
            "foodCategory": "canned soup",
            "foodId": "food_ayjzfd9bhvwqorb6m5iq3bekq7cj",
            "image": "https://www.edamam.com/food-img/12f/12f4b9a8e738f35b7dd787a5360e4a45.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 teaspoon Chinese chile paste",
            "weight": 5.104166666925555
          }
        ],
        "label": "Curry Mayonnaise",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/curry-mayonnaise-cb7810124de13e8a262788282abc2c45/curry",
        "source": "LA Times",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 9.896437499977866,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 3.5612008333267924,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 31.03,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 83.87951041666152,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 136.38522833333423,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 277.0562384615407,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 11.568819444439207,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 15.86031666666494,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 3.395281250018933,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 8.30251773052091,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 13.720833333335857,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 166.18574479166847,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 8.630692708338222,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 20.318476190453644,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 12.713598333321517,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 12.0927884615472,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 4.954868055538918,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 10.959466666674691,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 1.6707731481547643,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 5.625,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 15.608782051182532,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 6.882888889036233,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 2.6,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 5.719899305567975,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 8.486344696959245,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 98.96437499977867,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 10.683602499980378,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 6.718523333314143,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 93.09,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 1677.5902083332303,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 45.444324125001074,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 107.12527758333322,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 27.277045666666847,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 180.08655500000145,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 2.0823874999990575,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 3.965079166666235,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 13.581125000075732,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 13.581125000075732,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 390.21833333448274,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 57.627500000010606,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 3988.4578750000433,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 1.3809108333341154,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 142.2293333331755,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 6.356799166660759,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.1572062500001136,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 2.2241362500116617,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.059458416666467014,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 1.6439200000012038,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 15.036958333392878,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.135,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 0.2029141666653729,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 6.194600000132611,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.39,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 6.86387916668157,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 75.62014583373077,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 0.933497916665517,
            "unit": "mg"
          }
        },
        "totalTime": 0.0,
        "totalWeight": 333.98750000037296,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_cb7810124de13e8a262788282abc2c45",
        "url": "https://www.latimes.com/recipe/curry-mayonnaise",
        "yield": 1.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/83c6d362126e12c5ff37337e99e4e923?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 3210.669418525,
        "cautions": [],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [
          "High-Fiber",
          "Low-Carb"
        ],
        "digest": [
          {
            "daily": 355.69298900169235,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 288.63436712424993,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 57.72687342484999,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 1.121960727195,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 112.76548316440001,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 44.02027805505,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 231.2004428511,
            "unit": "g"
          },
          {
            "daily": 18.391964166666668,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 34.25841750000001,
                "unit": "g"
              },
              {
                "daily": 83.6699,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 20.917475,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 23.49288,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 55.1758925,
            "unit": "g"
          },
          {
            "daily": 443.407567182,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 221.703783591,
            "unit": "g"
          },
          {
            "daily": 289.165135875,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 867.495407625,
            "unit": "mg"
          },
          {
            "daily": 218.76433621681252,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 5250.3440692035,
            "unit": "mg"
          },
          {
            "daily": 36.71341983584579,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 367.134198358458,
            "unit": "mg"
          },
          {
            "daily": 77.5826279501335,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 325.84703739056073,
            "unit": "mg"
          },
          {
            "daily": 83.51914056892522,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 3925.399606739486,
            "unit": "mg"
          },
          {
            "daily": 82.38339644102804,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 14.829011359385047,
            "unit": "mg"
          },
          {
            "daily": 154.11003171732796,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 16.952103488906076,
            "unit": "mg"
          },
          {
            "daily": 274.3956427064286,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 1920.769498945,
            "unit": "mg"
          },
          {
            "daily": 505.52711920388884,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 4549.744072834999,
            "unit": "\u00b5g"
          },
          {
            "daily": 52.651965217777786,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 47.386768696000004,
            "unit": "mg"
          },
          {
            "daily": 86.716777175,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 1.0406013261,
            "unit": "mg"
          },
          {
            "daily": 130.78058863076922,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 1.7001476521999999,
            "unit": "mg"
          },
          {
            "daily": 524.3571488339687,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 83.897143813435,
            "unit": "mg"
          },
          {
            "daily": 364.71624248076927,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 4.741311152250001,
            "unit": "mg"
          },
          {
            "daily": 42.3863456525,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 169.54538261,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 169.54538261,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 149.40198686875001,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 3.58564768485,
            "unit": "\u00b5g"
          },
          {
            "daily": 15.422140579999999,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 2.313321087,
            "unit": "\u00b5g"
          },
          {
            "daily": 117.61761086999998,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 17.6426416305,
            "unit": "mg"
          },
          {
            "daily": 108.67431929374999,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 130.4091831525,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 1195.5364333937619,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Paleo",
          "Mediterranean",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Sulfite-Free",
          "Kosher",
          "Immuno-Supportive"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/8fd/8fd84bc2d9d5089a50cff9aa96e193bd.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=936020dafd6e44eb5e6e4842ff0117218a0c0e37b95df7f58b86db4c32095d3e",
        "images": {
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/8fd/8fd84bc2d9d5089a50cff9aa96e193bd.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=936020dafd6e44eb5e6e4842ff0117218a0c0e37b95df7f58b86db4c32095d3e",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/8fd/8fd84bc2d9d5089a50cff9aa96e193bd-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b90d45dace751d1ec300447d739a8ffae62ae86cd362edb5ead02f6f1d90382b",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/8fd/8fd84bc2d9d5089a50cff9aa96e193bd-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=21cd101c5722a7e06b950bdc19a1cbd691aa4f604b71e997433b1a55ee22e610",
            "width": 100
          }
        },
        "ingredientLines": [
          "1 3 1/2- to 4-pound chicken",
          "4 tablespoons olive oil",
          "2 1/2 teaspoons kosher salt",
          "3/4 teaspoon black pepper",
          "2 tablespoons curry powder",
          "8 carrots, halved lengthwise and cut into 1-inch pieces"
        ],
        "ingredients": [
          {
            "food": "chicken",
            "foodCategory": "Poultry",
            "foodId": "food_bmyxrshbfao9s1amjrvhoauob6mo",
            "image": "https://www.edamam.com/food-img/d33/d338229d774a743f7858f6764e095878.jpg",
            "measure": "pound",
            "quantity": 3.75,
            "text": "1 3 1/2- to 4-pound chicken",
            "weight": 1700.9713875
          },
          {
            "food": "olive oil",
            "foodCategory": "Oils",
            "foodId": "food_b1d1icuad3iktrbqby0hiagafaz7",
            "image": "https://www.edamam.com/food-img/4d6/4d651eaa8a353647746290c7a9b29d84.jpg",
            "measure": "tablespoon",
            "quantity": 4.0,
            "text": "4 tablespoons olive oil",
            "weight": 54.0
          },
          {
            "food": "kosher salt",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_a1vgrj1bs8rd1majvmd9ubz8ttkg",
            "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg",
            "measure": "teaspoon",
            "quantity": 2.5,
            "text": "2 1/2 teaspoons kosher salt",
            "weight": 12.135416667282188
          },
          {
            "food": "black pepper",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_b6ywzluaaxv02wad7s1r9ag4py89",
            "image": "https://www.edamam.com/food-img/c6e/c6e5c3bd8d3bc15175d9766971a4d1b2.jpg",
            "measure": "teaspoon",
            "quantity": 0.75,
            "text": "3/4 teaspoon black pepper",
            "weight": 2.175
          },
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "tablespoon",
            "quantity": 2.0,
            "text": "2 tablespoons curry powder",
            "weight": 12.6
          },
          {
            "food": "carrots",
            "foodCategory": "vegetables",
            "foodId": "food_ai215e5b85pdh5ajd4aafa3w2zm8",
            "image": "https://www.edamam.com/food-img/121/121e33fce0bb9546ed7d060b6c114e29.jpg",
            "measure": "<unit>",
            "quantity": 8.0,
            "text": "8 carrots, halved lengthwise and cut into 1-inch pieces",
            "weight": 488.0
          }
        ],
        "label": "Chicken Curry",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/chicken-curry-83c6d362126e12c5ff37337e99e4e923/curry",
        "source": "Real Simple",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 36.71341983584579,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 18.391964166666668,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 289.165135875,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 160.53347092624998,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 288.63436712424993,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 355.69298900169235,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 82.38339644102804,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 83.6699,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 42.3863456525,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 83.51914056892522,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 77.5826279501335,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 218.76433621681252,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 524.3571488339687,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 274.3956427064286,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 443.407567182,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 130.78058863076922,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 86.716777175,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 117.61761086999998,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 505.52711920388884,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 149.40198686875001,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 364.71624248076927,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 52.651965217777786,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 15.422140579999999,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 108.67431929374999,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 154.11003171732796,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 367.134198358458,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 55.1758925,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 34.25841750000001,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 867.495407625,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 3210.669418525,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 112.76548316440001,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 44.02027805505,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 57.72687342484999,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 231.2004428511,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 1.121960727195,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 14.829011359385047,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 20.917475,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 169.54538261,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 169.54538261,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 3925.399606739486,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 325.84703739056073,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 5250.3440692035,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 83.897143813435,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 1920.769498945,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 221.703783591,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 1.7001476521999999,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 23.49288,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 1.0406013261,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 17.6426416305,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 4549.744072834999,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 3.58564768485,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 4.741311152250001,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 47.386768696000004,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 2.313321087,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 130.4091831525,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 1195.5364333937619,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 16.952103488906076,
            "unit": "mg"
          }
        },
        "totalTime": 55.0,
        "totalWeight": 2268.3142565560747,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_83c6d362126e12c5ff37337e99e4e923",
        "url": "https://www.realsimple.com/food-recipes/browse-all-recipes/curry",
        "yield": 4.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/ad0f5e510b4e21140eeb419cea8e57b3?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 4760.323810666667,
        "cautions": [
          "Sulfites"
        ],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [],
        "digest": [
          {
            "daily": 200.39270955710953,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 149.13185130666665,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 29.82637026133333,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.00084,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 49.86359099721213,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 30.37075341345454,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 130.25526121212118,
            "unit": "g"
          },
          {
            "daily": 224.31065424242422,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 534.6601112121211,
                "unit": "g"
              },
              {
                "daily": 553.0874060606061,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 138.27185151515152,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 122.44415999999998,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 672.9319627272727,
            "unit": "g"
          },
          {
            "daily": 508.6041072727273,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 254.30205363636364,
            "unit": "g"
          },
          {
            "daily": 66.0,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 198.0,
            "unit": "mg"
          },
          {
            "daily": 38.12543188888889,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 915.0103653333333,
            "unit": "mg"
          },
          {
            "daily": 108.86833644848484,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 1088.6833644848484,
            "unit": "mg"
          },
          {
            "daily": 282.2378354978355,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 1185.398909090909,
            "unit": "mg"
          },
          {
            "daily": 244.23450420889745,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 11479.021697818182,
            "unit": "mg"
          },
          {
            "daily": 319.4055682962963,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 57.49300229333333,
            "unit": "mg"
          },
          {
            "daily": 382.9441322314051,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 42.123854545454556,
            "unit": "mg"
          },
          {
            "daily": 460.3777835497835,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 3222.6444848484844,
            "unit": "mg"
          },
          {
            "daily": 228.2951245791246,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 2054.6561212121214,
            "unit": "\u00b5g"
          },
          {
            "daily": 258.9965488215488,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 233.0968939393939,
            "unit": "mg"
          },
          {
            "daily": 429.0633434343434,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 5.148760121212121,
            "unit": "mg"
          },
          {
            "daily": 261.6489976689976,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 3.4014369696969693,
            "unit": "mg"
          },
          {
            "daily": 249.87482765151512,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 39.97997242424242,
            "unit": "mg"
          },
          {
            "daily": 542.5632027972027,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 7.053321636363636,
            "unit": "mg"
          },
          {
            "daily": 1300.319712121212,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 5201.278848484848,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 5201.278848484848,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 347.5,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 8.34,
            "unit": "\u00b5g"
          },
          {
            "daily": 2.0000000000000004,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.30000000000000004,
            "unit": "\u00b5g"
          },
          {
            "daily": 158.07885894949493,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 23.71182884242424,
            "unit": "mg"
          },
          {
            "daily": 1032.4550703434343,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 1238.946084412121,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 1693.6908090909087,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Mediterranean",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Sulfite-Free",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/009/009b842c052ede3889de3b77a58c80bd.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=f8872b21c3c1564882a4e4af04fc15c32382db66d98d5f69bebe3f42c8b23588",
        "images": {
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/009/009b842c052ede3889de3b77a58c80bd.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=f8872b21c3c1564882a4e4af04fc15c32382db66d98d5f69bebe3f42c8b23588",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/009/009b842c052ede3889de3b77a58c80bd-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=4c7b9fa66574aeefbcda5c1cc2052a511e3e0a6bd401e23769ab1d3655eed5a4",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/009/009b842c052ede3889de3b77a58c80bd-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=75a32c8f8972ff9761d5f2c2c7fb7434f24bcd381710d0e71389045cdc79cbe8",
            "width": 100
          }
        },
        "ingredientLines": [
          "olive oil",
          "300 g diced lean lamb shoulder",
          "1 tesapoon mustard seeds",
          "\u00bd teaspoon ground turmeric",
          "1 teaspoon chilli powder",
          "1 tablespoon Madras curry powder",
          "5 cm piece of ginger",
          "4 cloves of garlic",
          "3 onions",
          "10 curry leaves",
          "2 x 400 g tins of chickpeas",
          "1 organic vegetable stock cube",
          "1 x 400 g tin of quality plum tomatoes",
          "\u00bd x 400 g tin of light coconut milk",
          "200 g baby spinach",
          "1 bunch of fresh coriander"
        ],
        "ingredients": [
          {
            "food": "olive oil",
            "foodCategory": "Oils",
            "foodId": "food_b1d1icuad3iktrbqby0hiagafaz7",
            "image": "https://www.edamam.com/food-img/4d6/4d651eaa8a353647746290c7a9b29d84.jpg",
            "measure": null,
            "quantity": 0.0,
            "text": "olive oil",
            "weight": 39.86675151515151
          },
          {
            "food": "lean lamb shoulder",
            "foodCategory": "meats",
            "foodId": "food_bogydkib85lisba4or9febcru4om",
            "image": null,
            "measure": "gram",
            "quantity": 300.0,
            "text": "300 g diced lean lamb shoulder",
            "weight": 300.0
          },
          {
            "food": "mustard seeds",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_b0xqxo3a93nsz8a6ppdilau4ujwt",
            "image": "https://www.edamam.com/food-img/9ff/9ff9e6d04cbc71ff884f3212afa0adfd.jpg",
            "measure": null,
            "quantity": 0.0,
            "text": "1 tesapoon mustard seeds",
            "weight": 0.0
          },
          {
            "food": "ground turmeric",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_bc3ig84amucgmwba3vixyatnyd9b",
            "image": "https://www.edamam.com/food-img/03e/03eb469286b3caf1ae9c13e4eba13587.jpg",
            "measure": "teaspoon",
            "quantity": 0.5,
            "text": "\u00bd teaspoon ground turmeric",
            "weight": 1.5
          },
          {
            "food": "chilli powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_aii2sclb4r123rbfr2ybjasrl3nc",
            "image": "https://www.edamam.com/food-img/e6f/e6f19043caefc23b5feda5520076617e.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 teaspoon chilli powder",
            "weight": 2.7
          },
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoon Madras curry powder",
            "weight": 6.3
          },
          {
            "food": "piece of ginger",
            "foodCategory": "vegetables",
            "foodId": "food_bi2ki2xb5zmmvbaiwf7ztbgktzp6",
            "image": "https://www.edamam.com/food-img/b9c/b9c06ef451ef29513880af0a53ebbaa6.jpg",
            "measure": "<unit>",
            "quantity": 5.0,
            "text": "5 cm piece of ginger",
            "weight": 300.0
          },
          {
            "food": "garlic",
            "foodCategory": "vegetables",
            "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
            "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg",
            "measure": "clove",
            "quantity": 4.0,
            "text": "4 cloves of garlic",
            "weight": 12.0
          },
          {
            "food": "onions",
            "foodCategory": "vegetables",
            "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
            "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg",
            "measure": "<unit>",
            "quantity": 3.0,
            "text": "3 onions",
            "weight": 375.0
          },
          {
            "food": "curry leaves",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_asx39x4ayja4jab6ivj6zayvkblo",
            "image": "https://www.edamam.com/food-img/0f9/0f9f5f95df173e9ffaaff2977bef88f3.jpg",
            "measure": "<unit>",
            "quantity": 10.0,
            "text": "10 curry leaves",
            "weight": 6.0
          },
          {
            "food": "chickpeas",
            "foodCategory": "plant-based protein",
            "foodId": "food_baux5rqbkto336asd7w3lbbi1koo",
            "image": "https://www.edamam.com/food-img/520/520c62055515f730b8947e0e445fd2be.jpg",
            "measure": "gram",
            "quantity": 800.0,
            "text": "2 x 400 g tins of chickpeas",
            "weight": 800.0
          },
          {
            "food": "vegetable",
            "foodCategory": "vegetables",
            "foodId": "food_bitqzx8b319psvbib2dufarphbxy",
            "image": "https://www.edamam.com/food-img/f3f/f3fa6996eba331be219778406f67a5a3.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 organic vegetable stock cube",
            "weight": 287.8787878787879
          },
          {
            "food": "plum tomatoes",
            "foodCategory": "vegetables",
            "foodId": "food_ab8jymba5i5xv3apgymg7a90bxb5",
            "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg",
            "measure": "gram",
            "quantity": 400.0,
            "text": "1 x 400 g tin of quality plum tomatoes",
            "weight": 400.0
          },
          {
            "food": "light coconut milk",
            "foodCategory": "Vegan products",
            "foodId": "food_bfbjttnbf8cdwjabmp83ibuutl92",
            "image": "https://www.edamam.com/food-img/f85/f859cce57955d778ccb5d0224e08cf93.jpg",
            "measure": "gram",
            "quantity": 200.0,
            "text": "\u00bd x 400 g tin of light coconut milk",
            "weight": 200.0
          },
          {
            "food": "spinach",
            "foodCategory": "vegetables",
            "foodId": "food_aoceuc6bshdej1bbsdammbnj6l6o",
            "image": "https://www.edamam.com/food-img/e6e/e6e4be375c4554ce01c8ea75232efaa6.jpg",
            "measure": "gram",
            "quantity": 200.0,
            "text": "200 g baby spinach",
            "weight": 200.0
          },
          {
            "food": "fresh coriander",
            "foodCategory": "vegetables",
            "foodId": "food_alhzhuwb4lc7jnb5s6f02by60bzp",
            "image": "https://www.edamam.com/food-img/d57/d57e375b6ff99a90c7ee2b1990a1af36.jpg",
            "measure": "bunch",
            "quantity": 1.0,
            "text": "1 bunch of fresh coriander",
            "weight": 40.0
          }
        ],
        "label": "Lamb & chickpea curry",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/lamb-chickpea-curry-ad0f5e510b4e21140eeb419cea8e57b3/curry",
        "source": "Jamie Oliver",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 108.86833644848484,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 224.31065424242422,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 66.0,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 238.01619053333334,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 149.13185130666665,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 200.39270955710953,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 319.4055682962963,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 553.0874060606061,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 1300.319712121212,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 244.23450420889745,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 282.2378354978355,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 38.12543188888889,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 249.87482765151512,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 460.3777835497835,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 508.6041072727273,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 261.6489976689976,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 429.0633434343434,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 158.07885894949493,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 228.2951245791246,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 347.5,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 542.5632027972027,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 258.9965488215488,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 2.0000000000000004,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 1032.4550703434343,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 382.9441322314051,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 1088.6833644848484,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 672.9319627272727,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 534.6601112121211,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 198.0,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 4760.323810666667,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 49.86359099721213,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 30.37075341345454,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 29.82637026133333,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 130.25526121212118,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.00084,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 57.49300229333333,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 138.27185151515152,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 5201.278848484848,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 5201.278848484848,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 11479.021697818182,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 1185.398909090909,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 915.0103653333333,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 39.97997242424242,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 3222.6444848484844,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 254.30205363636364,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 3.4014369696969693,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 122.44415999999998,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 5.148760121212121,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 23.71182884242424,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 2054.6561212121214,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 8.34,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 7.053321636363636,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 233.0968939393939,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.30000000000000004,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 1238.946084412121,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 1693.6908090909087,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 42.123854545454556,
            "unit": "mg"
          }
        },
        "totalTime": 140.0,
        "totalWeight": 2971.2455393939395,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_ad0f5e510b4e21140eeb419cea8e57b3",
        "url": "http://www.jamieoliver.com/recipes/lamb-recipes/lamb-chickpea-curry/",
        "yield": 6.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/416b453ac07cc42ecd9a8775aa166451?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 931.4000000000001,
        "cautions": [],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [
          "Low-Carb",
          "Low-Sodium"
        ],
        "digest": [
          {
            "daily": 115.88812307692311,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 95.75396000000002,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 19.150792000000003,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 37.229656,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 11.785592000000001,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 75.32728000000002,
            "unit": "g"
          },
          {
            "daily": 17.687226666666668,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 44.65448000000001,
                "unit": "g"
              },
              {
                "daily": 33.6288,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 8.4072,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 8.274000000000001,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 53.06168,
            "unit": "g"
          },
          {
            "daily": 53.27936,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 26.63968,
            "unit": "g"
          },
          {
            "daily": 10.922666666666668,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 32.768,
            "unit": "mg"
          },
          {
            "daily": 16.200844,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 388.82025600000003,
            "unit": "mg"
          },
          {
            "daily": 17.263615558449867,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 172.63615558449868,
            "unit": "mg"
          },
          {
            "daily": 101.44988249587796,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 426.08950648268745,
            "unit": "mg"
          },
          {
            "daily": 21.295575571521265,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 1000.8920518614996,
            "unit": "mg"
          },
          {
            "daily": 86.3729841071492,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 15.547137139286857,
            "unit": "mg"
          },
          {
            "daily": 78.42755134789769,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 8.627030648268745,
            "unit": "mg"
          },
          {
            "daily": 120.97942857142858,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 846.8560000000001,
            "unit": "mg"
          },
          {
            "daily": 16.890666666666664,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 152.016,
            "unit": "\u00b5g"
          },
          {
            "daily": 8.217777777777778,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 7.396,
            "unit": "mg"
          },
          {
            "daily": 49.46866666666667,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.593624,
            "unit": "mg"
          },
          {
            "daily": 10.958769230769231,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.142464,
            "unit": "mg"
          },
          {
            "daily": 11.099400000000001,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 1.7759040000000001,
            "unit": "mg"
          },
          {
            "daily": 64.19138461538462,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 0.834488,
            "unit": "mg"
          },
          {
            "daily": 15.23,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 60.92,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 60.92,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.05333333333333334,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.00128,
            "unit": "\u00b5g"
          },
          {
            "daily": 1.5360000000000003,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.23040000000000002,
            "unit": "\u00b5g"
          },
          {
            "daily": 10.789333333333335,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 1.6184000000000003,
            "unit": "mg"
          },
          {
            "daily": 40.70066666666667,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 48.84080000000001,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 8.09598129653749,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Sugar-Conscious",
          "Vegetarian",
          "Pescatarian",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "No oil added",
          "Sulfite-Free",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/5e5/5e565421dfc0c6c4da2383b6f2c0a0c3.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=602282c05a7af1566404331017ef03d2249775d6226528f872fa82512a29d1bb",
        "images": {
          "LARGE": {
            "height": 600,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/5e5/5e565421dfc0c6c4da2383b6f2c0a0c3-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=818597ebbe2b232fa61e9e8c6ac445cb477bbb81d191081e05dfdffe41ed6620",
            "width": 600
          },
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/5e5/5e565421dfc0c6c4da2383b6f2c0a0c3.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=602282c05a7af1566404331017ef03d2249775d6226528f872fa82512a29d1bb",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/5e5/5e565421dfc0c6c4da2383b6f2c0a0c3-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=64c14b6c4c8feeb9c987fec81da69653d7bd1c1f6c679b910d9a037cb3973e3f",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/5e5/5e565421dfc0c6c4da2383b6f2c0a0c3-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=8ad46ef447f16a3a62427ecadafb91128cbaa3a8949d50e30fd6c657dab62f25",
            "width": 100
          }
        },
        "ingredientLines": [
          "1 cup raw cashews",
          "1 tablespoon ghee (Indian clarified butter) or homemade clarified butter",
          "2 dozen curry leaves",
          "Kosher or sea salt to taste"
        ],
        "ingredients": [
          {
            "food": "cashews",
            "foodCategory": "plant-based protein",
            "foodId": "food_aa3vawdabgm9zmapkfl78bk049g2",
            "image": "https://www.edamam.com/food-img/d4b/d4bc3f8024cac35e2039ef5ead328e11.jpg",
            "measure": "cup",
            "quantity": 1.0,
            "text": "1 cup raw cashews",
            "weight": 140.0
          },
          {
            "food": "clarified butter",
            "foodCategory": "Dairy",
            "foodId": "food_bt9uvvxacpohzjblxojh1behk63g",
            "image": "https://www.edamam.com/food-img/2b5/2b504c036c64481b224c9d74cc4a82e0.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoon ghee (Indian clarified butter) or homemade clarified butter",
            "weight": 12.8
          },
          {
            "food": "curry leaves",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_asx39x4ayja4jab6ivj6zayvkblo",
            "image": "https://www.edamam.com/food-img/0f9/0f9f5f95df173e9ffaaff2977bef88f3.jpg",
            "measure": "<unit>",
            "quantity": 24.0,
            "text": "2 dozen curry leaves",
            "weight": 14.399999999999999
          },
          {
            "food": "sea salt",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_a1vgrj1bs8rd1majvmd9ubz8ttkg",
            "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg",
            "measure": null,
            "quantity": 0.0,
            "text": "Kosher or sea salt to taste",
            "weight": 1.0032
          }
        ],
        "label": "Roasted Cashews & Curry Leaves",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/roasted-cashews-curry-leaves-416b453ac07cc42ecd9a8775aa166451/curry",
        "source": "San Francisco Gate",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 17.263615558449867,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 17.687226666666668,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 10.922666666666668,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 46.57000000000001,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 95.75396000000002,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 115.88812307692311,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 86.3729841071492,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 33.6288,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 15.23,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 21.295575571521265,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 101.44988249587796,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 16.200844,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 11.099400000000001,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 120.97942857142858,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 53.27936,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 10.958769230769231,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 49.46866666666667,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 10.789333333333335,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 16.890666666666664,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.05333333333333334,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 64.19138461538462,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 8.217777777777778,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 1.5360000000000003,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 40.70066666666667,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 78.42755134789769,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 172.63615558449868,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 53.06168,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 44.65448000000001,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 32.768,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 931.4000000000001,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 37.229656,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 11.785592000000001,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 19.150792000000003,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 75.32728000000002,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 15.547137139286857,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 8.4072,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 60.92,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 60.92,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 1000.8920518614996,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 426.08950648268745,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 388.82025600000003,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 1.7759040000000001,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 846.8560000000001,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 26.63968,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.142464,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 8.274000000000001,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.593624,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 1.6184000000000003,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 152.016,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.00128,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 0.834488,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 7.396,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.23040000000000002,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 48.84080000000001,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 8.09598129653749,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 8.627030648268745,
            "unit": "mg"
          }
        },
        "totalTime": 0.0,
        "totalWeight": 168.15064826874453,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_416b453ac07cc42ecd9a8775aa166451",
        "url": "http://www.sfgate.com/food/recipes/detail.html?rid=16582&sorig=qs",
        "yield": 4.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/611d58b2fcec4d894ed8c6443616d12e?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 1588.3293055560307,
        "cautions": [
          "Tree-Nuts",
          "Sulfites"
        ],
        "cuisineType": [
          "american"
        ],
        "dietLabels": [
          "High-Fiber",
          "Low-Carb",
          "Low-Sodium"
        ],
        "digest": [
          {
            "daily": 207.63058803420756,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 591.6822380555634,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 118.33644761111269,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 5.977676222222223,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 2.023258222222222,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 134.9598822222349,
            "unit": "g"
          },
          {
            "daily": 33.391992546319536,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 49.91940541673351,
                "unit": "g"
              },
              {
                "daily": 201.0262888889004,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 50.2565722222251,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 47.472285416704736,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 100.17597763895861,
            "unit": "g"
          },
          {
            "daily": 39.86223777781577,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 19.931118888907886,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 0.0,
            "unit": "mg"
          },
          {
            "daily": 12.19423784722612,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 292.6617083334269,
            "unit": "mg"
          },
          {
            "daily": 22.147527777872764,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 221.47527777872764,
            "unit": "mg"
          },
          {
            "daily": 51.72089947089947,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 217.2277777777778,
            "unit": "mg"
          },
          {
            "daily": 62.463640661938534,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 2935.791111111111,
            "unit": "mg"
          },
          {
            "daily": 77.06702469135804,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 13.872064444444447,
            "unit": "mg"
          },
          {
            "daily": 53.14137373737374,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 5.845551111111112,
            "unit": "mg"
          },
          {
            "daily": 92.54507936507936,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 647.8155555555555,
            "unit": "mg"
          },
          {
            "daily": 190.83266666666665,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 1717.494,
            "unit": "\u00b5g"
          },
          {
            "daily": 270.3458703704759,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 243.31128333342832,
            "unit": "mg"
          },
          {
            "daily": 46.672444444444444,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.5600693333333333,
            "unit": "mg"
          },
          {
            "daily": 32.39705982905982,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.42116177777777775,
            "unit": "mg"
          },
          {
            "daily": 34.85208333333333,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 5.576333333333333,
            "unit": "mg"
          },
          {
            "daily": 100.76801709401708,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 1.3099842222222222,
            "unit": "mg"
          },
          {
            "daily": 59.99944444444444,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 239.99777777777777,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 239.99777777777777,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 1.2295833333956991,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.18443750000935488,
            "unit": "\u00b5g"
          },
          {
            "daily": 18.704918518518518,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 2.8057377777777774,
            "unit": "mg"
          },
          {
            "daily": 43.32229629629629,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 51.98675555555555,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 819.8225318061648,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Keto-Friendly",
          "Vegan",
          "Vegetarian",
          "Pescatarian",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Sulfite-Free",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/40f/40f7e9a38aa59cc2d415519042e3d5ff.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=272415f3a49fc751a2fce563f0a212eed427435dac80a8f955c2288a10e40140",
        "images": {
          "LARGE": {
            "height": 600,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/40f/40f7e9a38aa59cc2d415519042e3d5ff-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=817bd140193820f17a6c1ab132a343abc5cc56a7c6d28df966806f9abfc6965e",
            "width": 600
          },
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/40f/40f7e9a38aa59cc2d415519042e3d5ff.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=272415f3a49fc751a2fce563f0a212eed427435dac80a8f955c2288a10e40140",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/40f/40f7e9a38aa59cc2d415519042e3d5ff-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=0cb686f0e593034cb600881ec418ec66c75d4531d6f3302255e6006063c33eb1",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/40f/40f7e9a38aa59cc2d415519042e3d5ff-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=cd3b1b6e02331703a39f05bd10b5355d2e35b62dda8fae160a17916185b4c332",
            "width": 100
          }
        },
        "ingredientLines": [
          "2 cups baby carrots",
          "2 peppers",
          "1 zucchini",
          "3 T plain soy yogurt",
          "1-2 t curry powder (to taste)",
          "1 heaping T of coconut oil"
        ],
        "ingredients": [
          {
            "food": "baby carrots",
            "foodCategory": "vegetables",
            "foodId": "food_bg0rlw7bt25ojiavi5k7dbv51765",
            "image": "https://www.edamam.com/food-img/954/9546f1fd29336cab2ecf552935d03206.jpg",
            "measure": "cup",
            "quantity": 2.0,
            "text": "2 cups baby carrots",
            "weight": 240.0
          },
          {
            "food": "peppers",
            "foodCategory": "vegetables",
            "foodId": "food_bz8rcwobbzm7zhb3wh2n7aznivou",
            "image": "https://www.edamam.com/food-img/629/629dc9fddc1f8aec27fa337dd6ce2b7c.jpg",
            "measure": "<unit>",
            "quantity": 2.0,
            "text": "2 peppers",
            "weight": 232.57777777777778
          },
          {
            "food": "zucchini",
            "foodCategory": "vegetables",
            "foodId": "food_avpihljbuwpd8ibbmahcabaros5s",
            "image": "https://www.edamam.com/food-img/f63/f637280594e4a731eccc1199194a8847.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 zucchini",
            "weight": 196.0
          },
          {
            "food": "soy yogurt",
            "foodCategory": "plant-based protein",
            "foodId": "food_bitht3aamrz5i0ahm3e2jbylhxfk",
            "image": "https://www.edamam.com/food-img/7af/7af62ce8a7266fafe0c8da8cd4958bca.png",
            "measure": "teaspoon",
            "quantity": 3.0,
            "text": "3 T plain soy yogurt",
            "weight": 14.187500000719606
          },
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "teaspoon",
            "quantity": 1.5,
            "text": "1-2 t curry powder (to taste)",
            "weight": 3.0
          },
          {
            "food": "coconut",
            "foodCategory": "plant-based protein",
            "foodId": "food_a0671ieawy879qbaiagcrapnmo84",
            "image": "https://www.edamam.com/food-img/a27/a27851affdcc1da2d94da0a4fbe3b062.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 heaping T of coconut oil",
            "weight": 397.0
          }
        ],
        "label": "Vegan Chickpea Coconut Curry",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/vegan-chickpea-coconut-curry-611d58b2fcec4d894ed8c6443616d12e/curry",
        "source": "Oh She Glows",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 22.147527777872764,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 33.391992546319536,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 79.41646527780154,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 591.6822380555634,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 207.63058803420756,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 77.06702469135804,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 201.0262888889004,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 59.99944444444444,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 62.463640661938534,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 51.72089947089947,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 12.19423784722612,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 34.85208333333333,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 92.54507936507936,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 39.86223777781577,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 32.39705982905982,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 46.672444444444444,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 18.704918518518518,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 190.83266666666665,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 100.76801709401708,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 270.3458703704759,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 1.2295833333956991,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 43.32229629629629,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 53.14137373737374,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 221.47527777872764,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 100.17597763895861,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 49.91940541673351,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 1588.3293055560307,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 5.977676222222223,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 2.023258222222222,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 118.33644761111269,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 134.9598822222349,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 13.872064444444447,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 50.2565722222251,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 239.99777777777777,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 239.99777777777777,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 2935.791111111111,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 217.2277777777778,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 292.6617083334269,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 5.576333333333333,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 647.8155555555555,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 19.931118888907886,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.42116177777777775,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 47.472285416704736,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.5600693333333333,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 2.8057377777777774,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 1717.494,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 1.3099842222222222,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 243.31128333342832,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.18443750000935488,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 51.98675555555555,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 819.8225318061648,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 5.845551111111112,
            "unit": "mg"
          }
        },
        "totalTime": 0.0,
        "totalWeight": 1082.7652777784974,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_611d58b2fcec4d894ed8c6443616d12e",
        "url": "http://ohsheglows.com/2009/09/01/food-blog-what-i-ate-day-1/",
        "yield": 8.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/5b44802ac6e3cbe8ed368e7ba3e476a3?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 1653.2649999999433,
        "cautions": [
          "Sulfites"
        ],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [
          "Low-Carb",
          "Low-Sodium"
        ],
        "digest": [
          {
            "daily": 274.71353846153755,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 133.22294999999949,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 26.644589999999898,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 44.765724999999996,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 106.87302249999995,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 178.5637999999994,
            "unit": "g"
          },
          {
            "daily": 3.737516666660737,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 7.263799999982985,
                "unit": "g"
              },
              {
                "daily": 15.794999999996907,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 3.948749999999227,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 6.285499999993504,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 11.212549999982212,
            "unit": "g"
          },
          {
            "daily": 3.4745499999981955,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 1.7372749999990977,
            "unit": "g"
          },
          {
            "daily": 30.03,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 90.09,
            "unit": "mg"
          },
          {
            "daily": 55.81760416666655,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 1339.6224999999972,
            "unit": "mg"
          },
          {
            "daily": 2.434499999998453,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 24.34499999998453,
            "unit": "mg"
          },
          {
            "daily": 5.308333333329651,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 22.294999999984533,
            "unit": "mg"
          },
          {
            "daily": 6.795691489356052,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 319.39749999973446,
            "unit": "mg"
          },
          {
            "daily": 5.266111111109965,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 0.9478999999997937,
            "unit": "mg"
          },
          {
            "daily": 3.937499999998828,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 0.4331249999998711,
            "unit": "mg"
          },
          {
            "daily": 6.4714285714256246,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 45.29999999997938,
            "unit": "mg"
          },
          {
            "daily": 20.761111111111113,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 186.85,
            "unit": "\u00b5g"
          },
          {
            "daily": 177.06527777766692,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 159.35874999990023,
            "unit": "mg"
          },
          {
            "daily": 6.719999999994845,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.08063999999993812,
            "unit": "mg"
          },
          {
            "daily": 8.679807692304717,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.11283749999996133,
            "unit": "mg"
          },
          {
            "daily": 7.920546874998532,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 1.2672874999997652,
            "unit": "mg"
          },
          {
            "daily": 29.184999999990875,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 0.3794049999998814,
            "unit": "mg"
          },
          {
            "daily": 15.677499999987111,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 62.70999999994844,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 62.70999999994844,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 16.07916666666409,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 2.411874999999614,
            "unit": "mg"
          },
          {
            "daily": 6.589166666666667,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 7.907,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 141.80517499976202,
            "unit": "g"
          }
        ],
        "dishType": [
          "condiments and sauces"
        ],
        "healthLabels": [
          "Sugar-Conscious",
          "Low Potassium",
          "Kidney-Friendly",
          "Keto-Friendly",
          "Vegetarian",
          "Pescatarian",
          "Paleo",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Sulfite-Free",
          "Kosher",
          "Immuno-Supportive"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/592/59208166868f710b93b596adc53233dd.jpeg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=0f62b9487e585b56a4525626c1555100bd285003ae1f08fc2fd97a1c843ae10b",
        "images": {
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/592/59208166868f710b93b596adc53233dd.jpeg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=0f62b9487e585b56a4525626c1555100bd285003ae1f08fc2fd97a1c843ae10b",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/592/59208166868f710b93b596adc53233dd-m.jpeg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=7b12914b0d729ff581a278b6e2dcd459ab3f42aa77c01b880475ece113af6002",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/592/59208166868f710b93b596adc53233dd-s.jpeg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=03f6a027fc943c3fff4581719c67fbec353928e74ea151c9c13384eea167d18b",
            "width": 100
          }
        },
        "ingredientLines": [
          "1 cup mayonnaise",
          "1 teaspoon curry powder",
          "1 tablespoon fresh lemon juice",
          "2 tablespoons grated onion",
          "1 red bell pepper"
        ],
        "ingredients": [
          {
            "food": "mayonnaise",
            "foodCategory": "condiments and sauces",
            "foodId": "food_bu8t61zaplle7dbrzk81dbygq0qj",
            "image": "https://www.edamam.com/food-img/577/577308a0422357885c94cc9b5f1f1862.jpg",
            "measure": "cup",
            "quantity": 1.0,
            "text": "1 cup mayonnaise",
            "weight": 231.0
          },
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 teaspoon curry powder",
            "weight": 2.0
          },
          {
            "food": "lemon juice",
            "foodCategory": "100% juice",
            "foodId": "food_bglm6vxahuauteb0n6ynfbg9eryu",
            "image": "https://www.edamam.com/food-img/e31/e310952d214e78a4cb8b73f30ceeaaf2.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoon fresh lemon juice",
            "weight": 15.2499999997422
          },
          {
            "food": "onion",
            "foodCategory": "vegetables",
            "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
            "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg",
            "measure": "tablespoon",
            "quantity": 2.0,
            "text": "2 tablespoons grated onion",
            "weight": 20.0
          },
          {
            "food": "red bell pepper",
            "foodCategory": "vegetables",
            "foodId": "food_a8g63g7ak6bnmvbu7agxibp4a0dy",
            "image": "https://www.edamam.com/food-img/4dc/4dc48b1a506d334b4ab6671b9d56a18f.jpeg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 red bell pepper",
            "weight": 119.0
          }
        ],
        "label": "Curry Dip",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/curry-dip-5b44802ac6e3cbe8ed368e7ba3e476a3/curry",
        "source": "Food Network",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 2.434499999998453,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 3.737516666660737,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 30.03,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 82.66324999999716,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 133.22294999999949,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 274.71353846153755,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 5.266111111109965,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 15.794999999996907,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 15.677499999987111,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 6.795691489356052,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 5.308333333329651,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 55.81760416666655,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 7.920546874998532,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 6.4714285714256246,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 3.4745499999981955,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 8.679807692304717,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 6.719999999994845,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 16.07916666666409,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 20.761111111111113,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 29.184999999990875,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 177.06527777766692,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 6.589166666666667,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 3.937499999998828,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 24.34499999998453,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 11.212549999982212,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 7.263799999982985,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 90.09,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 1653.2649999999433,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 44.765724999999996,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 106.87302249999995,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 26.644589999999898,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 178.5637999999994,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 0.9478999999997937,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 3.948749999999227,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 62.70999999994844,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 62.70999999994844,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 319.39749999973446,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 22.294999999984533,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 1339.6224999999972,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 1.2672874999997652,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 45.29999999997938,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 1.7372749999990977,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.11283749999996133,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 6.285499999993504,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.08063999999993812,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 2.411874999999614,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 186.85,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 0.3794049999998814,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 159.35874999990023,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 7.907,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 141.80517499976202,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 0.4331249999998711,
            "unit": "mg"
          }
        },
        "totalTime": 10.0,
        "totalWeight": 387.2499999997422,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_5b44802ac6e3cbe8ed368e7ba3e476a3",
        "url": "https://www.foodnetwork.com/recipes/paula-deen/curry-dip-recipe-1945699",
        "yield": 18.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/7aed82609f79393e54552e60576533be?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 225.952419,
        "cautions": [],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [
          "High-Protein",
          "Low-Carb"
        ],
        "digest": [
          {
            "daily": 12.237662984615385,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 11.51109624,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 2.302219248,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 2.565685891,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 1.1604866619999998,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 7.954480940000001,
            "unit": "g"
          },
          {
            "daily": 1.28261585,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 0.3654718499999996,
                "unit": "g"
              },
              {
                "daily": 13.929502800000002,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 3.4823757000000004,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 0.17718815999999998,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 3.84784755,
            "unit": "g"
          },
          {
            "daily": 67.80995182000001,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 33.904975910000005,
            "unit": "g"
          },
          {
            "daily": 42.60666666666667,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 127.82000000000001,
            "unit": "mg"
          },
          {
            "daily": 16.745093525500003,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 401.8822446120001,
            "unit": "mg"
          },
          {
            "daily": 4.0533039474087635,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 40.53303947408763,
            "unit": "mg"
          },
          {
            "daily": 12.732557028512774,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 53.47673951975366,
            "unit": "mg"
          },
          {
            "daily": 11.181326067192112,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 525.5223251580293,
            "unit": "mg"
          },
          {
            "daily": 48.57043534177058,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 8.742678361518704,
            "unit": "mg"
          },
          {
            "daily": 13.922137836139683,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 1.5314351619753652,
            "unit": "mg"
          },
          {
            "daily": 47.52824314285715,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 332.69770200000005,
            "unit": "mg"
          },
          {
            "daily": 2.973618111111111,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 26.762563,
            "unit": "\u00b5g"
          },
          {
            "daily": 11.484555555555557,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 10.336100000000002,
            "unit": "mg"
          },
          {
            "daily": 58.51718766666668,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.7022062520000001,
            "unit": "mg"
          },
          {
            "daily": 40.625416923076926,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.5281304200000001,
            "unit": "mg"
          },
          {
            "daily": 37.052051043750005,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 5.928328167000001,
            "unit": "mg"
          },
          {
            "daily": 81.07070607692309,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 1.0539191790000002,
            "unit": "mg"
          },
          {
            "daily": 11.27896825,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 45.115873,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 45.115873,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 52.56666666666667,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 1.2616,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 10.6366384,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 1.59549576,
            "unit": "mg"
          },
          {
            "daily": 5.94463775,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 7.1335653,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 125.96697384395075,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Sugar-Conscious",
          "Keto-Friendly",
          "Paleo",
          "Mediterranean",
          "DASH",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "No oil added",
          "Sulfite-Free",
          "Kosher"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/fe5/fe5078126db6022d48f2664b7eac9c42.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b5cc7886b60310ffbce582c857e21ff5d8bb5af4f5acafd9e923fe7d05b13348",
        "images": {
          "LARGE": {
            "height": 600,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/fe5/fe5078126db6022d48f2664b7eac9c42-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=f783a2f50c93a3c66c29046dece8332d87872c79d1d130efc46eea4f18f3c07e",
            "width": 600
          },
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/fe5/fe5078126db6022d48f2664b7eac9c42.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b5cc7886b60310ffbce582c857e21ff5d8bb5af4f5acafd9e923fe7d05b13348",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/fe5/fe5078126db6022d48f2664b7eac9c42-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d300c68aeb223053649117d9320e236e2e427b6b345da18ba87b109ce5088f87",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/fe5/fe5078126db6022d48f2664b7eac9c42-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=972ad73da20ae6be3ce25ed33d453b8d046839c7f4d7cabefbd147f01a9a9131",
            "width": 100
          }
        },
        "ingredientLines": [
          "1 tablespoon curry powder",
          "1 duck breast",
          "Salt and pepper"
        ],
        "ingredients": [
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoon curry powder",
            "weight": 6.3
          },
          {
            "food": "duck breast",
            "foodCategory": "Poultry",
            "foodId": "food_af1buxjb28zsaeal5gc0ia70r75d",
            "image": "https://www.edamam.com/food-img/d5e/d5e02c07028f66463b705d87b0e019d3.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 duck breast",
            "weight": 166.0
          },
          {
            "food": "Salt",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
            "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg",
            "measure": null,
            "quantity": 0.0,
            "text": "Salt and pepper",
            "weight": 1.0338
          },
          {
            "food": "pepper",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_b6ywzluaaxv02wad7s1r9ag4py89",
            "image": "https://www.edamam.com/food-img/c6e/c6e5c3bd8d3bc15175d9766971a4d1b2.jpg",
            "measure": null,
            "quantity": 0.0,
            "text": "Salt and pepper",
            "weight": 0.5169
          }
        ],
        "label": "Dinner Tonight: Duck Breast With Curry Seasoning",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/dinner-tonight-duck-breast-with-curry-seasoning-7aed82609f79393e54552e60576533be/curry",
        "source": "Serious Eats",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 4.0533039474087635,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 1.28261585,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 42.60666666666667,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 11.29762095,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 11.51109624,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 12.237662984615385,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 48.57043534177058,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 13.929502800000002,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 11.27896825,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 11.181326067192112,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 12.732557028512774,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 16.745093525500003,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 37.052051043750005,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 47.52824314285715,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 67.80995182000001,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 40.625416923076926,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 58.51718766666668,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 10.6366384,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 2.973618111111111,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 52.56666666666667,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 81.07070607692309,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 11.484555555555557,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 5.94463775,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 13.922137836139683,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 40.53303947408763,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 3.84784755,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 0.3654718499999996,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 127.82000000000001,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 225.952419,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 2.565685891,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 1.1604866619999998,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 2.302219248,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 7.954480940000001,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 8.742678361518704,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 3.4823757000000004,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 45.115873,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 45.115873,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 525.5223251580293,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 53.47673951975366,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 401.8822446120001,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 5.928328167000001,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 332.69770200000005,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 33.904975910000005,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.5281304200000001,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 0.17718815999999998,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.7022062520000001,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 1.59549576,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 26.762563,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 1.2616,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 1.0539191790000002,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 10.336100000000002,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 7.1335653,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 125.96697384395075,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 1.5314351619753652,
            "unit": "mg"
          }
        },
        "totalTime": 0.0,
        "totalWeight": 173.6009519753651,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_7aed82609f79393e54552e60576533be",
        "url": "http://www.seriouseats.com/recipes/2007/09/dinner-tonight-duck-breast-with-curry-seasoni.html",
        "yield": 2.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/38081c4906987babe7afa8ac290ce024?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 160.729,
        "cautions": [
          "Wheat",
          "Sulfites"
        ],
        "cuisineType": [
          "world"
        ],
        "dietLabels": [
          "Low-Fat",
          "Low-Sodium"
        ],
        "digest": [
          {
            "daily": 0.6335076923076922,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 0.554025,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 0.110805,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.0,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 0.079105,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 0.11303500000000001,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 0.41178,
            "unit": "g"
          },
          {
            "daily": 2.7079733333333333,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 6.76352,
                "unit": "g"
              },
              {
                "daily": 5.441599999999999,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 1.3604,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 4.279100000000001,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 4.1916,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 8.12392,
            "unit": "g"
          },
          {
            "daily": 0.8075600000000001,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 0.40378000000000003,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 0.0,
            "unit": "mg"
          },
          {
            "daily": 0.07383333333333333,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 1.7720000000000002,
            "unit": "mg"
          },
          {
            "daily": 4.098400000000001,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 40.98400000000001,
            "unit": "mg"
          },
          {
            "daily": 1.438095238095238,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 6.04,
            "unit": "mg"
          },
          {
            "daily": 0.6566382978723405,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 30.862000000000002,
            "unit": "mg"
          },
          {
            "daily": 11.625888888888888,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 2.09266,
            "unit": "mg"
          },
          {
            "daily": 1.6374545454545455,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 0.18012,
            "unit": "mg"
          },
          {
            "daily": 1.252,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 8.764,
            "unit": "mg"
          },
          {
            "daily": 1.651888888888889,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 14.867,
            "unit": "\u00b5g"
          },
          {
            "daily": 4.541111111111111,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 4.087000000000001,
            "unit": "mg"
          },
          {
            "daily": 0.3843333333333334,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 0.004612000000000001,
            "unit": "mg"
          },
          {
            "daily": 1.9690769230769232,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.025598,
            "unit": "mg"
          },
          {
            "daily": 0.623375,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 0.09974,
            "unit": "mg"
          },
          {
            "daily": 6.64,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 0.08632,
            "unit": "mg"
          },
          {
            "daily": 2.25625,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 9.025,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 9.025,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.035,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 0.00525,
            "unit": "mg"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 40.405860000000004,
            "unit": "g"
          }
        ],
        "dishType": [
          "alcohol cocktail"
        ],
        "healthLabels": [
          "Low Potassium",
          "Kidney-Friendly",
          "Keto-Friendly",
          "Vegan",
          "Vegetarian",
          "Pescatarian",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "No oil added",
          "Kosher",
          "Alcohol-Cocktail"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/c50/c506b2e0b4991fe15a2f32437c205b15.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=489a4958cfbbfde2845cf53a84934ae9c29c40812e9858c480fd0e7c2a223050",
        "images": {
          "LARGE": {
            "height": 600,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/c50/c506b2e0b4991fe15a2f32437c205b15-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a5c93c972dd318bd961987e63dd1615ba3767cba016c6189576fb2ed3e1f8731",
            "width": 600
          },
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/c50/c506b2e0b4991fe15a2f32437c205b15.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=489a4958cfbbfde2845cf53a84934ae9c29c40812e9858c480fd0e7c2a223050",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/c50/c506b2e0b4991fe15a2f32437c205b15-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=df9a2ffe35ec3dbc4b102bb931f970382606e81f179d70962ece50df05df350e",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/c50/c506b2e0b4991fe15a2f32437c205b15-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b2cb85095f739b3b858db45a4076ab567d43b41fe9f36bb091768c9ab5b226e4",
            "width": 100
          }
        },
        "ingredientLines": [
          "8 fresh curry leaves",
          "1 thin lemon wedge",
          "1 tsp sugar",
          "1/4 cup citrus vodka"
        ],
        "ingredients": [
          {
            "food": "curry leaves",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_asx39x4ayja4jab6ivj6zayvkblo",
            "image": "https://www.edamam.com/food-img/0f9/0f9f5f95df173e9ffaaff2977bef88f3.jpg",
            "measure": "<unit>",
            "quantity": 8.0,
            "text": "8 fresh curry leaves",
            "weight": 4.8
          },
          {
            "food": "lemon",
            "foodCategory": "fruit",
            "foodId": "food_a6uzc62astrxcgbtzyq59b6fncrr",
            "image": "https://www.edamam.com/food-img/70a/70acba3d4c734d7c70ef4efeed85dc8f.jpg",
            "measure": "wedge",
            "quantity": 1.0,
            "text": "1 thin lemon wedge",
            "weight": 3.5
          },
          {
            "food": "sugar",
            "foodCategory": "sugars",
            "foodId": "food_axi2ijobrk819yb0adceobnhm1c2",
            "image": "https://www.edamam.com/food-img/ecb/ecb3f5aaed96d0188c21b8369be07765.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 tsp sugar",
            "weight": 4.2
          },
          {
            "food": "vodka",
            "foodCategory": "liquors and cocktails",
            "foodId": "food_aqnx4i8aieyph2athk58cb3cr69w",
            "image": "https://www.edamam.com/food-img/e1a/e1a4708099e89fdadeb81c2d95deaa34.jpg",
            "measure": "cup",
            "quantity": 0.25,
            "text": "1/4 cup citrus vodka",
            "weight": 55.60000000000001
          }
        ],
        "label": "Curry-Leaf Mojito",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/curry-leaf-mojito-38081c4906987babe7afa8ac290ce024/curry",
        "source": "Men's Health",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 4.098400000000001,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 2.7079733333333333,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 8.03645,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 0.554025,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 0.6335076923076922,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 11.625888888888888,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 5.441599999999999,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 2.25625,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 0.6566382978723405,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 1.438095238095238,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 0.07383333333333333,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 0.623375,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 1.252,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 0.8075600000000001,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 1.9690769230769232,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.3843333333333334,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 0.035,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 1.651888888888889,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 6.64,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 4.541111111111111,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 0.0,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 1.6374545454545455,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 40.98400000000001,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 8.12392,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 6.76352,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 0.0,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 160.729,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 0.079105,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 0.11303500000000001,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 0.110805,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 0.41178,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.0,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 2.09266,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 1.3604,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 9.025,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 9.025,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 30.862000000000002,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 6.04,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 1.7720000000000002,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 0.09974,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 8.764,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 0.40378000000000003,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.025598,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 4.279100000000001,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 4.1916,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 0.004612000000000001,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 0.00525,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 14.867,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 0.08632,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 4.087000000000001,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 40.405860000000004,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 0.18012,
            "unit": "mg"
          }
        },
        "totalTime": 5.0,
        "totalWeight": 68.10000000000001,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_38081c4906987babe7afa8ac290ce024",
        "url": "https://www.menshealth.com/recipes/curry-leaf-mojito",
        "yield": 2.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/9b5f96f401262f079278a636ea0b9a03?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 3463.1024755499993,
        "cautions": [
          "Tree-Nuts",
          "Sulfites"
        ],
        "cuisineType": [
          "indian"
        ],
        "dietLabels": [
          "High-Fiber",
          "Low-Carb"
        ],
        "digest": [
          {
            "daily": 433.51905972307685,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 487.66772387525,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 97.53354477505,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 2.5174376535,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 98.92901943084998,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 45.81123279880001,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 281.78738881999993,
            "unit": "g"
          },
          {
            "daily": 15.123183865500001,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 29.335797376500004,
                "unit": "g"
              },
              {
                "daily": 64.13501688,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 16.03375422,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 15.8444996655,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 45.3695515965,
            "unit": "g"
          },
          {
            "daily": 367.9783910510001,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 183.98919552550004,
            "unit": "g"
          },
          {
            "daily": 302.39491333333336,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 907.18474,
            "unit": "mg"
          },
          {
            "daily": 163.75033207344998,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 3930.0079697627993,
            "unit": "mg"
          },
          {
            "daily": 39.409281583584814,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 394.09281583584817,
            "unit": "mg"
          },
          {
            "daily": 66.47167399787548,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 279.18103079107703,
            "unit": "mg"
          },
          {
            "daily": 86.35665566975779,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 4058.762816478616,
            "unit": "mg"
          },
          {
            "daily": 86.27145512530787,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 15.528861922555416,
            "unit": "mg"
          },
          {
            "daily": 273.93388076007,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 30.132726883607702,
            "unit": "mg"
          },
          {
            "daily": 258.1594555214286,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 1807.1161886500001,
            "unit": "mg"
          },
          {
            "daily": 21.48448863333334,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 193.36039770000002,
            "unit": "\u00b5g"
          },
          {
            "daily": 104.84364149444446,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 94.35927734500001,
            "unit": "mg"
          },
          {
            "daily": 324.3408116,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 3.8920897392,
            "unit": "mg"
          },
          {
            "daily": 235.66026130000003,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 3.0635833969000004,
            "unit": "mg"
          },
          {
            "daily": 346.86825038999996,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 55.49892006239999,
            "unit": "mg"
          },
          {
            "daily": 552.443650576923,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 7.1817674574999995,
            "unit": "mg"
          },
          {
            "daily": 31.801356937500003,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 127.20542775000001,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 127.20542775000001,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 179.54697979166667,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 4.309127515,
            "unit": "\u00b5g"
          },
          {
            "daily": 173.87707516666666,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 26.081561275,
            "unit": "\u00b5g"
          },
          {
            "daily": 63.81272547666667,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 9.571908821500001,
            "unit": "mg"
          },
          {
            "daily": 181.34558217916668,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 217.614698615,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 1159.4458572377152,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Paleo",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Tree-Nut-Free",
          "Soy-Free",
          "Fish-Free",
          "Shellfish-Free",
          "Crustacean-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Sulfite-Free"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/cef/cef6bfb453ab45e26b86d39809f633fd?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=203e9101ea35e874c56031632a4912788c006e99f92ce7ce8e069671a0a0ba3a",
        "images": {
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/cef/cef6bfb453ab45e26b86d39809f633fd?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=203e9101ea35e874c56031632a4912788c006e99f92ce7ce8e069671a0a0ba3a",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/cef/cef6bfb453ab45e26b86d39809f633fd-m?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=7a3ab6e475383095e5ab7ed69747ac71cdc7ba30c7ca5ee016f07e92dc70771a",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/cef/cef6bfb453ab45e26b86d39809f633fd-s?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a29445afd7aa267123b23a1213f4f01f6b887236bc9c5d7662402a575bde0ea8",
            "width": 100
          }
        },
        "ingredientLines": [
          "2.5 pounds pastured lamb spare ribs",
          "2 teaspoons kosher salt",
          "1 tablespoons curry powder (I use Maharajah Style Curry Powder)",
          "1 tablespoon coconut oil",
          "1 large yellow onion, coarsely chopped",
          "\u00bd pound ripe tomatoes",
          "5 cloves garlic, minced",
          "1 tablespoon curry powder (I use Maharajah Style Curry Powder)",
          "1 tablespoon kosher salt",
          "juice from 1 lemon",
          "1 \u00bc cup chopped cilantro, divided",
          "4 scallions, thinly sliced"
        ],
        "ingredients": [
          {
            "food": "ribs",
            "foodCategory": "meats",
            "foodId": "food_aue7j55a5pvxara45jh19a5lz3ba",
            "image": "https://www.edamam.com/food-img/e54/e548d7ddfea41f3ffa55cb712ae4e4a8.jpg",
            "measure": "pound",
            "quantity": 2.5,
            "text": "2.5 pounds pastured lamb spare ribs",
            "weight": 1133.980925
          },
          {
            "food": "kosher salt",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_a1vgrj1bs8rd1majvmd9ubz8ttkg",
            "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg",
            "measure": "teaspoon",
            "quantity": 2.0,
            "text": "2 teaspoons kosher salt",
            "weight": 9.70833333382575
          },
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoons curry powder (I use Maharajah Style Curry Powder)",
            "weight": 6.3
          },
          {
            "food": "coconut oil",
            "foodCategory": "Oils",
            "foodId": "food_b40ubq8a0enoidbcr1tmfbwgs6aw",
            "image": "https://www.edamam.com/food-img/3c9/3c97284c57e76e16093d51572b558be8.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoon coconut oil",
            "weight": 13.6
          },
          {
            "food": "yellow onion",
            "foodCategory": "vegetables",
            "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
            "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 large yellow onion, coarsely chopped",
            "weight": 150.0
          },
          {
            "food": "tomatoes",
            "foodCategory": "vegetables",
            "foodId": "food_a6k79rrahp8fe2b26zussa3wtkqh",
            "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg",
            "measure": "pound",
            "quantity": 0.5,
            "text": "\u00bd pound ripe tomatoes",
            "weight": 226.796185
          },
          {
            "food": "garlic",
            "foodCategory": "vegetables",
            "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
            "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg",
            "measure": "clove",
            "quantity": 5.0,
            "text": "5 cloves garlic, minced",
            "weight": 15.0
          },
          {
            "food": "curry powder",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_ao4koeoajh7yjxaq2knzrbv55y8o",
            "image": "https://www.edamam.com/food-img/9ce/9ce02a2887385fd2adaec8dd8adcf9c5.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoon curry powder (I use Maharajah Style Curry Powder)",
            "weight": 6.3
          },
          {
            "food": "kosher salt",
            "foodCategory": "Condiments and sauces",
            "foodId": "food_a1vgrj1bs8rd1majvmd9ubz8ttkg",
            "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tablespoon kosher salt",
            "weight": 14.562499999753793
          },
          {
            "food": "lemon",
            "foodCategory": "fruit",
            "foodId": "food_a6uzc62astrxcgbtzyq59b6fncrr",
            "image": "https://www.edamam.com/food-img/70a/70acba3d4c734d7c70ef4efeed85dc8f.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "juice from 1 lemon",
            "weight": 58.0
          },
          {
            "food": "cilantro",
            "foodCategory": "vegetables",
            "foodId": "food_alhzhuwb4lc7jnb5s6f02by60bzp",
            "image": "https://www.edamam.com/food-img/d57/d57e375b6ff99a90c7ee2b1990a1af36.jpg",
            "measure": "cup",
            "quantity": 1.25,
            "text": "1 \u00bc cup chopped cilantro, divided",
            "weight": 20.0
          },
          {
            "food": "scallions",
            "foodCategory": "vegetables",
            "foodId": "food_bknlkyzbuzo27pb11whr4bttkuy6",
            "image": "https://www.edamam.com/food-img/b89/b89986ed6aa466285bdd99bac34b3c46.jpg",
            "measure": "<unit>",
            "quantity": 4.0,
            "text": "4 scallions, thinly sliced",
            "weight": 60.0
          }
        ],
        "label": "Pressure Cooker Indian Curry Lamb Spareribs recipes",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/pressure-cooker-indian-curry-lamb-spareribs-recipes-9b5f96f401262f079278a636ea0b9a03/curry",
        "source": "Nom Nom Paleo",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 39.409281583584814,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 15.123183865500001,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 302.39491333333336,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 173.15512377749997,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 487.66772387525,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 433.51905972307685,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 86.27145512530787,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 64.13501688,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 31.801356937500003,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 86.35665566975779,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 66.47167399787548,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 163.75033207344998,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 346.86825038999996,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 258.1594555214286,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 367.9783910510001,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 235.66026130000003,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 324.3408116,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 63.81272547666667,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 21.48448863333334,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 179.54697979166667,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 552.443650576923,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 104.84364149444446,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 173.87707516666666,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 181.34558217916668,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 273.93388076007,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 394.09281583584817,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 45.3695515965,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 29.335797376500004,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 907.18474,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 3463.1024755499993,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 98.92901943084998,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 45.81123279880001,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 97.53354477505,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 281.78738881999993,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 2.5174376535,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 15.528861922555416,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 16.03375422,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 127.20542775000001,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 127.20542775000001,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 4058.762816478616,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 279.18103079107703,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 3930.0079697627993,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 55.49892006239999,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 1807.1161886500001,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 183.98919552550004,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 3.0635833969000004,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 15.8444996655,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 3.8920897392,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 9.571908821500001,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 193.36039770000002,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 4.309127515,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 7.1817674574999995,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 94.35927734500001,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 26.081561275,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 217.614698615,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 1159.4458572377152,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 30.132726883607702,
            "unit": "mg"
          }
        },
        "totalTime": 60.0,
        "totalWeight": 1697.627354107701,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_9b5f96f401262f079278a636ea0b9a03",
        "url": "http://nomnompaleo.com/post/18713738423/pressure-cooker-indian-curry-lamb-spareribs?mc_cid=f2bb81331e&mc_eid=50556986f5",
        "yield": 2.0
      }
    },
    {
      "_links": {
        "self": {
          "href": "https://api.edamam.com/api/recipes/v2/2f6ad7442c3853e72770662ec6c51bcb?type=public&app_id=2b4bf0c3&app_key=b7db63449d8aef2259fb1681f9fb9a75",
          "title": "Self"
        }
      },
      "recipe": {
        "calories": 2141.8354732554317,
        "cautions": [
          "Sulfites",
          "FODMAP"
        ],
        "cuisineType": [
          "south east asian"
        ],
        "dietLabels": [],
        "digest": [
          {
            "daily": 72.70107634947685,
            "hasRDI": true,
            "label": "Fat",
            "schemaOrgTag": "fatContent",
            "sub": [
              {
                "daily": 113.72260522029664,
                "hasRDI": true,
                "label": "Saturated",
                "schemaOrgTag": "saturatedFatContent",
                "tag": "FASAT",
                "total": 22.74452104405933,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Trans",
                "schemaOrgTag": "transFatContent",
                "tag": "FATRN",
                "total": 0.12552369480000003,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Monounsaturated",
                "schemaOrgTag": null,
                "tag": "FAMS",
                "total": 11.65692926303282,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Polyunsaturated",
                "schemaOrgTag": null,
                "tag": "FAPU",
                "total": 4.292561885864559,
                "unit": "g"
              }
            ],
            "tag": "FAT",
            "total": 47.255699627159956,
            "unit": "g"
          },
          {
            "daily": 101.80844346305976,
            "hasRDI": true,
            "label": "Carbs",
            "schemaOrgTag": "carbohydrateContent",
            "sub": [
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Carbs (net)",
                "schemaOrgTag": null,
                "tag": "CHOCDF.net",
                "total": 286.6340586741702,
                "unit": "g"
              },
              {
                "daily": 75.16508686003637,
                "hasRDI": true,
                "label": "Fiber",
                "schemaOrgTag": "fiberContent",
                "tag": "FIBTG",
                "total": 18.791271715009092,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars",
                "schemaOrgTag": "sugarContent",
                "tag": "SUGAR",
                "total": 25.270325446438427,
                "unit": "g"
              },
              {
                "daily": 0.0,
                "hasRDI": false,
                "label": "Sugars, added",
                "schemaOrgTag": null,
                "tag": "SUGAR.added",
                "total": 0.0,
                "unit": "g"
              }
            ],
            "tag": "CHOCDF",
            "total": 305.4253303891793,
            "unit": "g"
          },
          {
            "daily": 239.82000900596415,
            "hasRDI": true,
            "label": "Protein",
            "schemaOrgTag": "proteinContent",
            "tag": "PROCNT",
            "total": 119.91000450298208,
            "unit": "g"
          },
          {
            "daily": 244.08210515284662,
            "hasRDI": true,
            "label": "Cholesterol",
            "schemaOrgTag": "cholesterolContent",
            "tag": "CHOLE",
            "total": 732.2463154585399,
            "unit": "mg"
          },
          {
            "daily": 32.19348542515946,
            "hasRDI": true,
            "label": "Sodium",
            "schemaOrgTag": "sodiumContent",
            "tag": "NA",
            "total": 772.643650203827,
            "unit": "mg"
          },
          {
            "daily": 68.557067808453,
            "hasRDI": true,
            "label": "Calcium",
            "schemaOrgTag": null,
            "tag": "CA",
            "total": 685.57067808453,
            "unit": "mg"
          },
          {
            "daily": 105.87199615190215,
            "hasRDI": true,
            "label": "Magnesium",
            "schemaOrgTag": null,
            "tag": "MG",
            "total": 444.66238383798907,
            "unit": "mg"
          },
          {
            "daily": 78.87545299286184,
            "hasRDI": true,
            "label": "Potassium",
            "schemaOrgTag": null,
            "tag": "K",
            "total": 3707.1462906645065,
            "unit": "mg"
          },
          {
            "daily": 111.5580739927,
            "hasRDI": true,
            "label": "Iron",
            "schemaOrgTag": null,
            "tag": "FE",
            "total": 20.080453318686,
            "unit": "mg"
          },
          {
            "daily": 95.50509914428262,
            "hasRDI": true,
            "label": "Zinc",
            "schemaOrgTag": null,
            "tag": "ZN",
            "total": 10.50556090587109,
            "unit": "mg"
          },
          {
            "daily": 220.1009323346258,
            "hasRDI": true,
            "label": "Phosphorus",
            "schemaOrgTag": null,
            "tag": "P",
            "total": 1540.7065263423806,
            "unit": "mg"
          },
          {
            "daily": 301.9311637437443,
            "hasRDI": true,
            "label": "Vitamin A",
            "schemaOrgTag": null,
            "tag": "VITA_RAE",
            "total": 2717.380473693699,
            "unit": "\u00b5g"
          },
          {
            "daily": 141.06090526783302,
            "hasRDI": true,
            "label": "Vitamin C",
            "schemaOrgTag": null,
            "tag": "VITC",
            "total": 126.95481474104973,
            "unit": "mg"
          },
          {
            "daily": 187.36998355642388,
            "hasRDI": true,
            "label": "Thiamin (B1)",
            "schemaOrgTag": null,
            "tag": "THIA",
            "total": 2.2484398026770864,
            "unit": "mg"
          },
          {
            "daily": 30.39315287695209,
            "hasRDI": true,
            "label": "Riboflavin (B2)",
            "schemaOrgTag": null,
            "tag": "RIBF",
            "total": 0.39511098740037714,
            "unit": "mg"
          },
          {
            "daily": 118.35996508547883,
            "hasRDI": true,
            "label": "Niacin (B3)",
            "schemaOrgTag": null,
            "tag": "NIA",
            "total": 18.937594413676614,
            "unit": "mg"
          },
          {
            "daily": 116.95351444711812,
            "hasRDI": true,
            "label": "Vitamin B6",
            "schemaOrgTag": null,
            "tag": "VITB6A",
            "total": 1.5203956878125358,
            "unit": "mg"
          },
          {
            "daily": 317.0517940638195,
            "hasRDI": true,
            "label": "Folate equivalent (total)",
            "schemaOrgTag": null,
            "tag": "FOLDFE",
            "total": 1268.207176255278,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folate (food)",
            "schemaOrgTag": null,
            "tag": "FOLFD",
            "total": 216.4821762552781,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Folic acid",
            "schemaOrgTag": null,
            "tag": "FOLAC",
            "total": 618.8249999999999,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.24013290667072654,
            "hasRDI": true,
            "label": "Vitamin B12",
            "schemaOrgTag": null,
            "tag": "VITB12",
            "total": 0.005763189760097437,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": true,
            "label": "Vitamin D",
            "schemaOrgTag": null,
            "tag": "VITD",
            "total": 0.0,
            "unit": "\u00b5g"
          },
          {
            "daily": 76.17781150331068,
            "hasRDI": true,
            "label": "Vitamin E",
            "schemaOrgTag": null,
            "tag": "TOCPHA",
            "total": 11.4266717254966,
            "unit": "mg"
          },
          {
            "daily": 20.156171685447596,
            "hasRDI": true,
            "label": "Vitamin K",
            "schemaOrgTag": null,
            "tag": "VITK1",
            "total": 24.187406022537115,
            "unit": "\u00b5g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Sugar alcohols",
            "schemaOrgTag": null,
            "tag": "Sugar.alcohol",
            "total": 0.0,
            "unit": "g"
          },
          {
            "daily": 0.0,
            "hasRDI": false,
            "label": "Water",
            "schemaOrgTag": null,
            "tag": "WATER",
            "total": 999.7122083307165,
            "unit": "g"
          }
        ],
        "dishType": [
          "main course"
        ],
        "healthLabels": [
          "Pescatarian",
          "Dairy-Free",
          "Gluten-Free",
          "Wheat-Free",
          "Egg-Free",
          "Peanut-Free",
          "Soy-Free",
          "Pork-Free",
          "Red-Meat-Free",
          "Celery-Free",
          "Mustard-Free",
          "Sesame-Free",
          "Lupine-Free",
          "Mollusk-Free",
          "Alcohol-Free",
          "Sulfite-Free"
        ],
        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/d9b/d9bea22b3c3dde2174a56a4faf08c551.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=8fb39ce4ff19415fd3c27c5ed92d0502abda17a4fd22049851c6ae11922f4bb9",
        "images": {
          "REGULAR": {
            "height": 300,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/d9b/d9bea22b3c3dde2174a56a4faf08c551.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=8fb39ce4ff19415fd3c27c5ed92d0502abda17a4fd22049851c6ae11922f4bb9",
            "width": 300
          },
          "SMALL": {
            "height": 200,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/d9b/d9bea22b3c3dde2174a56a4faf08c551-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=83ce40a8e1edd1e8c8de3d34f0294df46a378c8c285f184bacbe6249d2814fe2",
            "width": 200
          },
          "THUMBNAIL": {
            "height": 100,
            "url": "https://edamam-product-images.s3.amazonaws.com/web-img/d9b/d9bea22b3c3dde2174a56a4faf08c551-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJGMEQCIGNf8pgzddl9RkBcU%2FhJbaFK0h9KpsUgnnuXJOEgcgblAiAcZKGx9V6xDfgZSQa1zxuVbEQGvnvz2aPOrdxacKwQmSrMBAg0EAAaDDE4NzAxNzE1MDk4NiIMxXVCMBCnP1b6ei2SKqkE4atz8l4CqMtLxrzzTETqq684LHZvegkVmRKuC95W%2BQdRqeADp%2BARfX08OmKq08e2zZRtNXfRDcc7GYVOi7qEVyv2lhooxlkjKn6hoptohVVNtKzpozNw9QU7Ng%2F9UwK2for7WeFyal1mDfj%2BOh3sTNVyEYtYlaZoDCazfw%2Fl%2FKVh8hYCAJGUGR3FBCRQkmhawrvJdUh%2Bu7fuerCsO5PI34r526%2BcRCq7AtiG1b61LzMqpsGRWLDdV99nIkhJS3lB083wG3bcxcajjr4n%2BzTjRuF2aTQgX%2BoExyunYEUIyRSitmwzVptyahfBpIGOME%2BkNsC3fDY%2FbPv9zDc%2Bbq6h0jq0ytX%2BLEsUA0aRSGoZLnpD%2FDYNURp8GScrGRo7xjvNcspRVhSV50WzkATuDTkRZsGdiT5RS5q0iBrNzagvEB7oXKGggUbPadPXE0l%2FFTiTD2QgOMpsumGTvntTFKUhp6pjSYRxFnBCjCtW8ROou6S4lwk%2BXgr9VhnJXqBZw9B1CXX1%2BjMCeF9hgrhlZbKGSma%2FdrrXvPM%2BRGds6Jw5UrOoAlMkNIqHru7eYgxkQDSrEfzK5yG7OA9X5vhFA3fSSwJ7EtpsHNsG71wpEB0E9XJOcEa9Yv9NWj6WMDSDwXVqjhkggKvdtef6XyPUznIi2DSdG4gb%2Bj%2BppcN2WZtyoMrO4Wd1Y5BNEA6VMsKNPUU%2FlNA5%2BN7ojHX9Gz2isI%2Bt6XlOb7I4itFEbTDM99mbBjqqAVqr8x13YESVu78LiifnJnzj7aN6rgyhRbuNsZsX3WMFvEIEkaQJpnq8jPhAcdtgOH8khJ5OiIebd6huW%2BDKfn2A7kY9bK1%2FB3GBE%2FHtFgrjQbeE9xL7HCX8DOhRqGsBd%2FINITOcAxxlYYRev7lEpzI2em4jBJ488BmEncPlOEkpcYbgshmJiX7sUIBRkCMjrAWUfoxBW4lWxaiA2LFru8BS6y3euE%2FuKNWT&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221117T185653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJT44HSMH%2F20221117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c11bc0fdf6986912220895a337ea3efb81af7963a004de8a2594e85f16efdfd0",
            "width": 100
          }
        },
        "ingredientLines": [
          "1\u00bd c. jasmine rice",
          "1 package butternut squash",
          "4 oz. green beans",
          "1 tbsp. vegetable oil",
          "1 small onion",
          "1 tbsp. red curry paste",
          "1 tsp. red curry paste",
          "1 lb. large shrimp",
          "1 can light coconut milk"
        ],
        "ingredients": [
          {
            "food": "jasmine rice",
            "foodCategory": "grains",
            "foodId": "food_a3g7g0kb4xvknbbdl91t8a19a6ci",
            "image": "https://www.edamam.com/food-img/e35/e35ea1529983a3db51a32a1afa7b3837.jpg",
            "measure": "cup",
            "quantity": 1.5,
            "text": "1\u00bd c. jasmine rice",
            "weight": 277.5
          },
          {
            "food": "butternut squash",
            "foodCategory": "vegetables",
            "foodId": "food_baga212bywb6n2as0ylgkaf8fcok",
            "image": "https://www.edamam.com/food-img/0aa/0aa76af7d957416d766248b145aa5cbe.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 package butternut squash",
            "weight": 500.0
          },
          {
            "food": "green beans",
            "foodCategory": "vegetables",
            "foodId": "food_aceucvpau4a8v6atkx5eabxyoqdn",
            "image": "https://www.edamam.com/food-img/891/89135f10639878a2360e6a33c9af3d91.jpg",
            "measure": "ounce",
            "quantity": 4.0,
            "text": "4 oz. green beans",
            "weight": 113.3980925
          },
          {
            "food": "vegetable oil",
            "foodCategory": "Oils",
            "foodId": "food_bt1mzi2ah2sfg8bv7no1qai83w8s",
            "image": "https://www.edamam.com/food-img/6e5/6e51a63a6300a8ea1b4c4cc68dfaba33.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tbsp. vegetable oil",
            "weight": 14.0
          },
          {
            "food": "onion",
            "foodCategory": "vegetables",
            "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
            "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg",
            "measure": "<unit>",
            "quantity": 1.0,
            "text": "1 small onion",
            "weight": 70.0
          },
          {
            "food": "red curry paste",
            "foodCategory": "condiments and sauces",
            "foodId": "food_aojdol2are6zg7af2nincbe87jot",
            "image": "https://www.edamam.com/food-img/b6a/b6a9ebae5850f42eca0253827603ef9c.jpg",
            "measure": "tablespoon",
            "quantity": 1.0,
            "text": "1 tbsp. red curry paste",
            "weight": 16.0
          },
          {
            "food": "red curry paste",
            "foodCategory": "condiments and sauces",
            "foodId": "food_aojdol2are6zg7af2nincbe87jot",
            "image": "https://www.edamam.com/food-img/b6a/b6a9ebae5850f42eca0253827603ef9c.jpg",
            "measure": "teaspoon",
            "quantity": 1.0,
            "text": "1 tsp. red curry paste",
            "weight": 5.333333333694016
          },
          {
            "food": "shrimp",
            "foodCategory": "seafood",
            "foodId": "food_bjap0xzbf5x6s3azkpwtfb14i25u",
            "image": "https://www.edamam.com/food-img/4df/4df0fd62e878ed84b387b9e3ab48f2dc.jpg",
            "measure": "pound",
            "quantity": 1.0,
            "text": "1 lb. large shrimp",
            "weight": 453.59237
          },
          {
            "food": "light coconut milk",
            "foodCategory": "Vegan products",
            "foodId": "food_bfbjttnbf8cdwjabmp83ibuutl92",
            "image": "https://www.edamam.com/food-img/f85/f859cce57955d778ccb5d0224e08cf93.jpg",
            "measure": "can",
            "quantity": 1.0,
            "text": "1 can light coconut milk",
            "weight": 387.3
          }
        ],
        "label": "Thai Shrimp Curry",
        "mealType": [
          "lunch/dinner"
        ],
        "shareAs": "http://www.edamam.com/recipe/thai-shrimp-curry-2f6ad7442c3853e72770662ec6c51bcb/curry",
        "source": "Delish",
        "totalDaily": {
          "CA": {
            "label": "Calcium",
            "quantity": 68.557067808453,
            "unit": "%"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 101.80844346305976,
            "unit": "%"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 244.08210515284662,
            "unit": "%"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 107.09177366277157,
            "unit": "%"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 113.72260522029664,
            "unit": "%"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 72.70107634947685,
            "unit": "%"
          },
          "FE": {
            "label": "Iron",
            "quantity": 111.5580739927,
            "unit": "%"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 75.16508686003637,
            "unit": "%"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 317.0517940638195,
            "unit": "%"
          },
          "K": {
            "label": "Potassium",
            "quantity": 78.87545299286184,
            "unit": "%"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 105.87199615190215,
            "unit": "%"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 32.19348542515946,
            "unit": "%"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 118.35996508547883,
            "unit": "%"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 220.1009323346258,
            "unit": "%"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 239.82000900596415,
            "unit": "%"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 30.39315287695209,
            "unit": "%"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 187.36998355642388,
            "unit": "%"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 76.17781150331068,
            "unit": "%"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 301.9311637437443,
            "unit": "%"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.24013290667072654,
            "unit": "%"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 116.95351444711812,
            "unit": "%"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 141.06090526783302,
            "unit": "%"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "%"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 20.156171685447596,
            "unit": "%"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 95.50509914428262,
            "unit": "%"
          }
        },
        "totalNutrients": {
          "CA": {
            "label": "Calcium",
            "quantity": 685.57067808453,
            "unit": "mg"
          },
          "CHOCDF": {
            "label": "Carbs",
            "quantity": 305.4253303891793,
            "unit": "g"
          },
          "CHOCDF.net": {
            "label": "Carbohydrates (net)",
            "quantity": 286.6340586741702,
            "unit": "g"
          },
          "CHOLE": {
            "label": "Cholesterol",
            "quantity": 732.2463154585399,
            "unit": "mg"
          },
          "ENERC_KCAL": {
            "label": "Energy",
            "quantity": 2141.8354732554317,
            "unit": "kcal"
          },
          "FAMS": {
            "label": "Monounsaturated",
            "quantity": 11.65692926303282,
            "unit": "g"
          },
          "FAPU": {
            "label": "Polyunsaturated",
            "quantity": 4.292561885864559,
            "unit": "g"
          },
          "FASAT": {
            "label": "Saturated",
            "quantity": 22.74452104405933,
            "unit": "g"
          },
          "FAT": {
            "label": "Fat",
            "quantity": 47.255699627159956,
            "unit": "g"
          },
          "FATRN": {
            "label": "Trans",
            "quantity": 0.12552369480000003,
            "unit": "g"
          },
          "FE": {
            "label": "Iron",
            "quantity": 20.080453318686,
            "unit": "mg"
          },
          "FIBTG": {
            "label": "Fiber",
            "quantity": 18.791271715009092,
            "unit": "g"
          },
          "FOLAC": {
            "label": "Folic acid",
            "quantity": 618.8249999999999,
            "unit": "\u00b5g"
          },
          "FOLDFE": {
            "label": "Folate equivalent (total)",
            "quantity": 1268.207176255278,
            "unit": "\u00b5g"
          },
          "FOLFD": {
            "label": "Folate (food)",
            "quantity": 216.4821762552781,
            "unit": "\u00b5g"
          },
          "K": {
            "label": "Potassium",
            "quantity": 3707.1462906645065,
            "unit": "mg"
          },
          "MG": {
            "label": "Magnesium",
            "quantity": 444.66238383798907,
            "unit": "mg"
          },
          "NA": {
            "label": "Sodium",
            "quantity": 772.643650203827,
            "unit": "mg"
          },
          "NIA": {
            "label": "Niacin (B3)",
            "quantity": 18.937594413676614,
            "unit": "mg"
          },
          "P": {
            "label": "Phosphorus",
            "quantity": 1540.7065263423806,
            "unit": "mg"
          },
          "PROCNT": {
            "label": "Protein",
            "quantity": 119.91000450298208,
            "unit": "g"
          },
          "RIBF": {
            "label": "Riboflavin (B2)",
            "quantity": 0.39511098740037714,
            "unit": "mg"
          },
          "SUGAR": {
            "label": "Sugars",
            "quantity": 25.270325446438427,
            "unit": "g"
          },
          "SUGAR.added": {
            "label": "Sugars, added",
            "quantity": 0.0,
            "unit": "g"
          },
          "Sugar.alcohol": {
            "label": "Sugar alcohol",
            "quantity": 0.0,
            "unit": "g"
          },
          "THIA": {
            "label": "Thiamin (B1)",
            "quantity": 2.2484398026770864,
            "unit": "mg"
          },
          "TOCPHA": {
            "label": "Vitamin E",
            "quantity": 11.4266717254966,
            "unit": "mg"
          },
          "VITA_RAE": {
            "label": "Vitamin A",
            "quantity": 2717.380473693699,
            "unit": "\u00b5g"
          },
          "VITB12": {
            "label": "Vitamin B12",
            "quantity": 0.005763189760097437,
            "unit": "\u00b5g"
          },
          "VITB6A": {
            "label": "Vitamin B6",
            "quantity": 1.5203956878125358,
            "unit": "mg"
          },
          "VITC": {
            "label": "Vitamin C",
            "quantity": 126.95481474104973,
            "unit": "mg"
          },
          "VITD": {
            "label": "Vitamin D",
            "quantity": 0.0,
            "unit": "\u00b5g"
          },
          "VITK1": {
            "label": "Vitamin K",
            "quantity": 24.187406022537115,
            "unit": "\u00b5g"
          },
          "WATER": {
            "label": "Water",
            "quantity": 999.7122083307165,
            "unit": "g"
          },
          "ZN": {
            "label": "Zinc",
            "quantity": 10.50556090587109,
            "unit": "mg"
          }
        },
        "totalTime": 30.0,
        "totalWeight": 1837.123795833694,
        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_2f6ad7442c3853e72770662ec6c51bcb",
        "url": "http://www.delish.com/cooking/recipe-ideas/recipes/a30586/thai-shrimp-curry-recipe/",
        "yield": 4.0
      }
    }
  ],
  "to": 20
}"""
list_books = {"史记":"司马迁",
              "红与黑":"司汤",
              "悲惨世界":"雨果",
              "西游记":"吴承恩",
              "本草纲目":"李时珍"}
list_books["昆虫记"] = "法布尔"
list_books["水浒传"] = "施耐庵"
list_books["红与黑"] = "司汤达"
list_books.pop("西游记")
del list_books["悲惨世界"]
print(list_books)


dict={
    "BMW":"2020",
    "Ford":"2019",
    "Toyota":"2018",
    "BMW": "2012",
    "Honda": "2015"

}
for key1 in sorted(dict,key=dict.get):
    print(key1,dict[key1])
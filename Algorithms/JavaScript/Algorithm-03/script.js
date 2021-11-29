let a = prompt("1 ci bir eded yaz")
let b = prompt("2 ci bir eded daha yaz , ve neticede men senin daxil etdiyin 2 ədədin 30-70 arasında olmasını yoxlayacam ve rəqəmlərin hər ikisinin , yalnız birinin və ya heç birinin aralıqinda olub-olmamasi haqqinda melumati print edecem console-a")

Number(a)
Number(b)

if (a > 30 && a < 70 && b > 30 && b < 70) {
    console.log("Ededlerin ikiside 30 ile 70 araliqindadir ! ")
} else if (a < 30 && 30 < b && b < 70) {
    console.log("1 ci eded 30 dan kicik amma 2 ci eded 30 ile 70 araliqindadir !")
} else if (a == 30 && b > 30 && b < 70) {
    console.log("1 ci eded 30 a beraber amma 2 ci eded 30 ile 70 araliqindadir !")
} else if (a == 30 && b == 70) {
    console.log("1 ci eded 30 a 2 ci ise 70 e beraberdir !")
} else if (a == 30 && b == 30) {
    console.log("Ededlerin 2 side 30 a beraberdir")
} else if (a == 70 && b == 70) {
    console.log("Ededlerin 2 side 70 a beraberdir")
} else if (a == 70 && b == 30) {
    console.log("1 ci eded 70 a 2 ci ise 30 e beraberdir !")
} else if (a > 30 && a < 70 && b == 70) {
    console.log("1 ci eded 30 ile 70 araliqindadir lakin 2 ci 70 e beraberdir !")
} else if (a > 30 && a < 70 && b > 70) {
    console.log("1 ci eded 30 ile 70 araliqindadir lakin 2 ci 70 den boyukdur !")
} else if (a > 30 && a < 70 && b > 70) {
    console.log("1 ci eded 30 ile 70 araliqindadir lakin 2 ci 70 den boyukdur !")
} else {
    console.log("Normal eded yaz aeeeeeee yekebas !")
}
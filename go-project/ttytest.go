package main 
import(
	"fmt"
	"os"
)

func main(){
	fmt.Println("【ターミナルから読み取ります】")

	var input string 
	fmt.Print("入力してください: ")

	fmt.Fscan(os.Stdin, &input)
	fmt.Println("あなたが入力したのは", input)
}
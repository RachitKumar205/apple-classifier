package cmd

import (
	"fmt"
	"log"
	"net/http"
	"os/exec"

	"github.com/jpoz/groq"
)

func ExecModel(url string) []byte {

	cmd := exec.Command("/bin/sh", "run.sh", url)
	response, err := cmd.Output()

	if err != nil {

		log.Println("errorlol", err)

	}

	prompt := string(response)

	client := groq.NewClient(groq.WithAPIKey("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"))
	comp, err := client.CreateChatCompletion(groq.CompletionCreateParams{

		Model: "llama-3.1-70b-versatile",
		Messages: []groq.Message{
			{
				Role:    "user",
				Content: fmt.Sprintf(`Classify the list of apple descriptions as good and bad based on ripeness and output the number of good apples and total apples. Only output valid json. For example, {"good_apples":5, "total_apples": 9}. Do not output anything else, before or after. Here is the data: %s`, prompt),
			},
		},
	})

	if err != nil {

		log.Println(err)

	}

	log.Println(comp.Choices[0].Message.Content)
	r := []byte(comp.Choices[0].Message.Content)

	return r

}

func Execute() {

	mux := http.NewServeMux()
	mux.HandleFunc("/imgurl", func(w http.ResponseWriter, r *http.Request) {

		if r.Method != http.MethodGet {

			return

		}

		url := r.URL.Query().Get("url")
		resp := ExecModel(url)

		w.Write(resp)

	})

	log.Println("listening on localhost :8000")
	http.ListenAndServe(":8000", mux)

}

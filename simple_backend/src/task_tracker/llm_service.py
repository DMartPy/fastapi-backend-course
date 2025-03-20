import requests
from typing import Optional

class LLMService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.cloudflare.com/client/v4/accounts/84345449372656be4199f39b5fd4a832/ai/run/"
        self.model = "@cf/meta/llama-3-8b-instruct"

    def get_task_solution(self, task_text: str) -> Optional[str]:
        """Получить рекомендации по решению задачи от LLM."""
        try:
            inputs = [
                {"role": "system", "content": "Ты - помощник по планированию задач. Твоя задача - анализировать задачи и предлагать пошаговые планы их решения."},
                {"role": "user", "content": f"Проанализируй следующую задачу и предложи пошаговый план её решения: {task_text}"}
            ]

            response = requests.post(
                f"{self.base_url}{self.model}",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={"messages": inputs}
            )
            
            if response.status_code == 200:
                result = response.json()
                print("Ответ от API:", result)  # для отладки
                return result.get("result", {}).get("response", "")
            else:
                print(f"Ошибка при запросе к LLM: {response.status_code}")
                print("Ответ сервера:", response.text)  # для отладки
                return None
                
        except Exception as e:
            print(f"Ошибка при работе с LLM: {str(e)}")
            return None 
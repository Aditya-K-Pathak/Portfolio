url = 'http://16.171.137.22:8000/api/editor/'

import requests
import concurrent.futures

payload = {
    'code': '''
import java.util.Scanner;

public class temp {
    private static int calculateFactorial(int n) {
        int ans = 1;
        for (int i = 1; i <= n; i++) {
            ans = ans * i;
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();
        scanner.close();
        
        System.out.println(calculateFactorial(n));
    }
}

''',
    'lang': 'Python',
    'input': '10'
}
# Function to make an API request
def make_api_request(url):
    response = requests.post(url, json=payload)
    return response.json()

# Function to test API load tolerance
def test_load_tolerance(url, num_requests):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks to the thread pool
        future_to_url = {executor.submit(make_api_request, url): url for _ in range(num_requests)}

        # Process completed tasks
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                status_code = future.result()
                print(f"Request to {url} completed with status code: {status_code}")
            except Exception as e:
                print(f"Request to {url} failed with exception: {e}")

if __name__ == "__main__":
    # URL of the API to test
    api_url = url

    # Number of concurrent requests to simulate
    num_requests = 1

    # Test load tolerance of the API
    test_load_tolerance(api_url, num_requests)

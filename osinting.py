import requests
from bs4 import BeautifulSoup
import re

class OSINTFramework:
    def __init__(self, target):
        self.target = target
    
    def search_google(self, query):
        url = f"https://www.google.com/search?q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for result in soup.find_all("div", class_="rc"):
            title = result.find("h3").text
            link = result.find("a")["href"]
            results.append({"title": title, "link": link})
        return results
    
    def search_twitter(self, query):
        url = f"https://twitter.com/search?q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for result in soup.find_all("div", class_="tweet"):
            text = result.find("p", class_="tweet-text").text
            results.append({"text": text})
        return results
    
    def search_linkedin(self, query):
        url = f"https://www.linkedin.com/search/results/all/?keywords={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for result in soup.find_all("div", class_="search-result__info"):
            title = result.find("a", class_="search-result__result-link").text
            link = result.find("a", class_="search-result__result-link")["href"]
            results.append({"title": title, "link": link})
        return results
    
    def search_github(self, query):
        url = f"https://github.com/search?q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for result in soup.find_all("div", class_="repo-list-item"):
            title = result.find("a", class_="v-align-middle").text
            link = result.find("a", class_="v-align-middle")["href"]
            results.append({"title": title, "link": link})
        return results
    
    def search_facebook(self, query):
        url = f"https://www.facebook.com/search/top/?q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for result in soup.find_all("div", class_="rq0escxv l9j0dhe7 du4w35lb"):
            title = result.find("div", class_="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rx9719w0").text
            link = result.find("a")["href"]
            results.append({"title": title, "link": link})
        return results
    
    def search_instagram(self, query):
        url = f"https://www.instagram.com/web/search/topsearch/?query={query}"
        response = requests.get(url)
        data = response.json()
        results = []
        for result in data["users"]:
            username = result["user"]["username"]
            link = f"https://www.instagram.com/{username}/"
            results.append({"username": username, "link": link})
        return results
    
    def search_all(self):
        google_results = self.search_google(self.target)
        twitter_results = self.search_twitter(self.target)
        linkedin_results = self.search_linkedin(self.target)
        github_results = self.search_github(self.target)
        facebook_results = self.search_facebook(self.target)
        instagram_results = self.search_instagram(self.target)
        
        results = {
            "google": google_results,
            "twitter": twitter_results,
            "linkedin": linkedin_results,
            "github": github_results,
            "facebook": facebook_results,
            "instagram": instagram_results
        }
        
        return results

# Example usage
framework = OSINTFramework("John Doe")
results = framework.search_all()
print(results)

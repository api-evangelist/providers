---
aid: microsoft-linkedin
name: Microsoft LinkedIn
description: LinkedIn, owned by Microsoft, provides APIs for accessing professional networking data, marketing and advertising capabilities, talent solutions, and consumer features including sign-in with LinkedIn.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Marketing
  - Microsoft
  - Professional Networking
  - Recruiting
  - Social Network
url: https://raw.githubusercontent.com/api-evangelist/microsoft-linkedin/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-linkedin:marketing-api
    name: LinkedIn Marketing API
    tags:
      - Advertising
      - Marketing
      - Social Media
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.linkedin.com/v2/
    humanURL: https://learn.microsoft.com/en-us/linkedin/marketing/
    properties:
      - url: https://learn.microsoft.com/en-us/linkedin/marketing/
        type: Documentation
    description: The LinkedIn Marketing API enables programmatic management of LinkedIn advertising campaigns, audience targeting, creative assets, and performance reporting. Developers can create sponsored content, manage campaign groups, configure conversion tracking, and retrieve analytics data for marketing optimization.
  - aid: microsoft-linkedin:consumer-api
    name: LinkedIn Consumer API
    tags:
      - Profiles
      - Sharing
      - Social Network
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.linkedin.com/v2/
    humanURL: https://learn.microsoft.com/en-us/linkedin/consumer/
    properties:
      - url: https://learn.microsoft.com/en-us/linkedin/consumer/
        type: Documentation
    description: The LinkedIn Consumer API provides access to member profiles, sign-in with LinkedIn, and content sharing capabilities. Developers can implement social sign-on, retrieve basic profile information, and enable users to share content to their LinkedIn feeds from external applications.
  - aid: microsoft-linkedin:talent-solutions-api
    name: LinkedIn Talent Solutions API
    tags:
      - HR
      - Recruiting
      - Talent
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.linkedin.com/v2/
    humanURL: https://learn.microsoft.com/en-us/linkedin/talent/
    properties:
      - url: https://learn.microsoft.com/en-us/linkedin/talent/
        type: Documentation
    description: The LinkedIn Talent Solutions API provides access to recruiting and talent management capabilities. It enables integration with applicant tracking systems, job posting management, candidate search, and recruiter workflow automation for enterprise hiring processes.
common:
  - type: Portal
    url: https://developer.linkedin.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/linkedin/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication
  - type: Rate Limits
    url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/rate-limits
  - type: Terms of Service
    url: https://www.linkedin.com/legal/l/api-terms-of-use
  - type: Privacy Policy
    url: https://www.linkedin.com/legal/privacy-policy
  - type: Support
    url: https://www.linkedin.com/help/linkedin
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

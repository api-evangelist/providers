---
aid: agify-io
name: Agify.io
description: Agify.io is a simple REST API that predicts the age of a person based on their first name. Using a large dataset of name-age associations, it returns an estimated age along with a count of how many data points were used and the name's country-localized variant when a country code is provided. Supports batch requests for up to 10 names per call. Used for demographics research, content personalization, and marketing segmentation.
url: https://raw.githubusercontent.com/api-evangelist/agify-io/refs/heads/main/apis.yml
humanURL: https://agify.io/
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
tags:
  - Age Prediction
  - Name Analysis
  - Demographics
  - REST API
created: '2025-01-07'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: agify-io:predict-age-api
    name: Agify.io Predict Age API
    description: Predict the age of a person based on their first name. Returns an estimated age, data count used for the prediction, and optionally a country-localized estimate. Supports single name and batch requests of up to 10 names.
    humanURL: https://agify.io/documentation
    baseURL: https://api.agify.io
    tags:
      - Age Prediction
      - Name
      - Demographics
    properties:
      - type: Documentation
        url: https://agify.io/documentation
      - type: Pricing
        url: https://agify.io/#pricing
common:
  - type: Portal
    url: https://agify.io/
  - type: Documentation
    url: https://agify.io/documentation
  - type: Pricing
    url: https://agify.io/#pricing
  - type: Features
    data:
      - name: Name-Based Age Prediction
        description: Estimates a person's age from their first name using a large statistical dataset of name-age associations.
      - name: Country Localization
        description: Accepts an optional ISO 3166-1 country code to return country-specific age predictions for the given name.
      - name: Batch Processing
        description: Supports up to 10 names per API request using array parameter syntax for efficient bulk predictions.
      - name: Rate Limit Headers
        description: Returns X-Rate-Limit-Limit, X-Rate-Limit-Remaining, and X-Rate-Limit-Reset headers to track API usage and quota.
      - name: Free Tier
        description: Free access for up to 100 requests per day without an API key, making it easy to evaluate the service.
  - type: UseCases
    data:
      - name: Demographics Research
        description: Analyze name datasets to estimate age distributions across a user base for research and analytics purposes.
      - name: Content Personalization
        description: Tailor content or product recommendations based on estimated age derived from a user's provided first name.
      - name: Marketing Segmentation
        description: Segment leads and customers by estimated age group for targeted marketing campaigns without requiring date-of-birth collection.
      - name: Form Pre-Fill Assistance
        description: Provide age-range hints during user registration to improve form completion rates and data accuracy.
  - type: Integrations
    data:
      - name: Genderize.io
        description: Sibling API that predicts gender based on first name — commonly used alongside Agify for demographic profiling.
      - name: Nationalize.io
        description: Sibling API that predicts nationality from first name, completing a demographic analysis trifecta with Agify and Genderize.
  - type: RateLimits
    data:
      - name: Free
        description: 100 requests per day, no API key required
      - name: Basic
        description: 25,000 requests per month for $20
      - name: Standard
        description: 250,000 requests per month for $60
      - name: Plus
        description: 2,500,000 requests per month for $180
      - name: Premium
        description: 25,000,000 requests per month for $540
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

---
aid: clutch
url: https://raw.githubusercontent.com/api-evangelist/clutch/refs/heads/main/apis.yml
name: Clutch
x-type: company
tags:
  - B2B Reviews
  - Business Services
  - IT Services
  - Ratings
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-24'
modified: '2026-04-23'
specificationVersion: '0.19'
description: Clutch is a B2B ratings and reviews platform that helps businesses identify and connect with service providers, including IT services, marketing agencies, and software developers. Clutch (acquired by Twilio's parent ecosystem and operating at clutch.co) publishes verified client reviews and rankings for software development, digital marketing, IT services, design, and consulting firms. Clutch makes verified review and ratings data available to approved partners and verified vendors through a partner API for integration into vendor websites, CRM systems, and marketing tools.
apis:
  - aid: clutch:clutch-api
    name: Clutch API
    tags:
      - B2B Reviews
      - Business Services
      - IT Services
      - Ratings
      - Reviews
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clutch.co
    humanURL: https://clutch.co/developers
    properties:
      - url: https://clutch.co/developers
        type: Documentation
      - url: https://clutch.co/developers#authentication
        type: Authentication
      - url: https://clutch.co/profile/claim
        type: Portal
    description: The Clutch API provides programmatic access to Clutch's B2B ratings and reviews platform, covering IT services, marketing agencies, and business service providers. Approved vendors and partners can retrieve company profiles, ratings, reviews, and service categories. The API enables integration of Clutch review data into third-party applications, websites, and CRM systems, allowing service providers to display verified client reviews and ratings badges. Authentication is handled via API keys issued to approved partners and vendors.
    x-features:
      - name: Verified Reviews
        description: Programmatic retrieval of verified Clutch client reviews for vendor profiles.
      - name: Ratings and Rankings
        description: Access to numeric ratings and category rankings (e.g. "Top Software Developers in NYC").
      - name: Company Profiles
        description: Retrieve metadata about service-provider profiles - services, locations, focus.
      - name: Review Badges
        description: Generate embeddable badges showing rating, review count, and category placement.
      - name: Service Categories
        description: Browse the canonical Clutch service taxonomy used to classify providers.
    x-useCases:
      - name: Embed Reviews on Vendor Sites
        description: Display verified Clutch reviews and ratings widgets on a service provider's own site.
      - name: CRM Reputation Sync
        description: Sync Clutch review data into HubSpot, Salesforce, or other CRMs for sales enablement.
      - name: Business Intelligence
        description: Pull review/rating trends into BI dashboards to track reputation over time.
      - name: Lead Quality Signal
        description: Use Clutch presence and rating data as a quality signal in B2B prospecting workflows.
common:
  - url: https://clutch.co/
    name: Clutch Website
    type: Website
  - url: https://clutch.co/developers
    name: API Documentation
    type: Documentation
  - url: https://clutch.co/profile/claim
    name: Claim Your Profile
    type: Portal
  - url: https://clutch.co/register
    name: Sign Up
    type: SignUp
  - url: https://clutch.co/login
    name: Login
    type: Login
  - url: https://clutch.co/pricing
    name: Pricing
    type: Pricing
  - url: https://clutch.co/developers#authentication
    name: Authentication
    type: Authentication
  - url: https://clutch.co/about-clutch
    name: About Clutch
    type: About
  - url: https://clutch.co/contact-us
    name: Contact Us
    type: Support
  - url: https://clutch.co/legal/terms-of-use
    name: Terms of Use
    type: TermsOfService
  - url: https://clutch.co/legal/privacy-policy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://clutch.co/blog
    name: Clutch Blog
    type: Blog
  - url: https://twitter.com/clutch_co
    name: Clutch on X (Twitter)
    type: X
  - url: https://www.linkedin.com/company/clutch-co
    name: Clutch on LinkedIn
    type: LinkedIn
  - url: https://www.facebook.com/clutch.co
    name: Clutch on Facebook
    type: Facebook
  - url: https://www.instagram.com/clutch.co
    name: Clutch on Instagram
    type: Instagram
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

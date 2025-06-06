---
aid: hubspot
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/hubspot.yml
apis:
  - aid: hubspot:hubspot-domains-api
    name: HubSpot Domains API
    tags:
      - Domains
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/overview
    overlays:
      - url: >-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/domains-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/domains
        type: Documentation
      - url: properties/hubspot-domains-api-openapi.yml
        type: OpenAPI
    description: |-

      These endpoints allow you to return information about the domains
      connected to a particular HubSpot CMS site. You can return data for a list
      of domains or specify a domain by ID.
  - aid: hubspot:hubspot-source-code-api
    name: HubSpot Source Code API
    tags:
      - Sources
      - Code
      - Environments
      - Content
      - Path
      - Validate
      - Extract
      - Async
      - Task
      - Status
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/source-code
    overlays:
      - url: >-

          overlays/https://api.hubspot.com/public/api/spec/v1/specs/cms/v3/source-code-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/source-code
        type: Documentation
      - url: properties/hubspot-source-code-api-openapi.yml
        type: OpenAPI
    description: |-

      Endpoints for interacting with files in the CMS Developer File System.
      These files include HTML templates, CSS, JS, modules, and other assets
      which are used to create CMS content.
  - aid: hubspot:hubspot-posts-api
    name: HubSpot Posts API
    tags:
      - Blogs
      - Posts
      - Schedules
      - Batch
      - Read
      - Multi
      - Language
      - Blog  Posts
      - Objects
      - Draft
      - Revisions
      - Restore
      - Variations
      - Clone
      - Detach
      - Groups
      - Live
      - Archive
      - Reset
      - Attach
      - Set
      - Primary
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/blog-post
    overlays:
      - url: >-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/blogs/blog-posts-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/blog-post
        type: Documentation
      - url: properties/hubspot-posts-api-openapi.yml
        type: OpenAPI
    description: |-

      Use these endpoints for interacting with Blog Posts, Blog Authors, and
      Blog Tags.
  - aid: hubspot:hubspot-authors-api
    name: HubSpot Authors API
    tags:
      - Blogs
      - Authors
      - Objects
      - Batch
      - Multi
      - Language
      - Detach
      - Groups
      - Set
      - Primary
      - Archive
      - Read
      - Attach
      - Variations
      - Languages
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/blog-authors
    overlays:
      - url: >-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/blogs/authors-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/blog-authors
        type: Documentation
      - url: properties/hubspot-authors-api-openapi.yml
        type: OpenAPI
    description: |-

      Use the blog authors API to manage author information for your blog
      posts. 
  - aid: hubspot:hubspot-url-redirects-api
    name: HubSpot URL Redirects API
    tags:
      - Redirects
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/url-redirects
    overlays:
      - url: >-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/url-redirects-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/url-redirects
        type: Documentation
      - url: properties/hubspot-url-redirects-api-openapi.yml
        type: OpenAPI
    description: |-

      URL redirects allow you to redirect traffic from a HubSpot-hosted page or
      blog post to any URL. You can also update URL redirects in bulk and use a
      flexible pattern redirect to dynamically update the structure of URLs.
name: HubSpot
tags:
  - CRM
  - Marketing
  - Sales
  - Content
  - Commerce
  - Operations
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://api.hubspot.com/api-catalog-public/v1/apis
    type: Index
  - url: https://developers.hubspot.com/
    type: Portal
  - url: https://developers.hubspot.com/docs/api/overview
    type: Documentation
  - url: https://developers.hubspot.com/changelog
    type: Change Log
  - url: https://community.hubspot.com/t5/HubSpot-Developers/ct-p/developers
    type: Forums
  - url: https://developers.hubspot.com/slack
    type: Slack
  - url: https://developers.hubspot.com/blog
    type: Blog
  - url: https://offers.hubspot.com/developer-newsletter-signup
    type: Newsletter
  - url: https://www.hubspot.com/developer-community-events
    type: Events
  - url: https://ecosystem.hubspot.com/marketplace/apps
    type: Marketplace
  - url: https://legal.hubspot.com/privacy-policy
    type: Privacy Policy
  - url: https://legal.hubspot.com/terms-of-service
    type: Terms of Service
  - url: https://developers.hubspot.com/
    name: HubSpot Developers
    type: Portal
    description: 'null'
  - url: https://developers.hubspot.com/docs/getting-started/overview
    name: Getting started overview | HubSpot
    type: GettingStarted
    description: 'null'
  - url: https://developers.hubspot.com/docs/guides/api
    name: Guides | HubSpot
    type: Guide
    description: 'null'
  - url: https://developers.hubspot.com/docs/reference/api/overview
    name: HubSpot API reference | HubSpot
    type: Documentation
    description: 'null'
  - url: https://app.hubspot.com/login
    name: HubSpot Login and Sign in
    type: Login
    description: 'null'
  - url: >-
      https://offers.hubspot.com/crm-platform-demo?hubs_signup-url=https://offers.hubspot.com/crm-platform-demo&hubs_signup-cta=login-demo-existing
    name: HubSpot Customer Platform Demo
    type: RequestDemo
    description: 'null'
  - url: >-
      https://legal.hubspot.com/privacy-policy?hubs_content=offers.hubspot.com/crm-platform-demo&hubs_content-cta=Privacy+Policy&hubs_signup-url=https://offers.hubspot.com/crm-platform-demo&hubs_signup-cta=login-demo-existing&_gl=1*1qpu9zs*_gcl_au*NDQ3NTExOTU2LjE3NDkxNjkxNzA.*FPAU*NDQ3NTExOTU2LjE3NDkxNjkxNzA.*_ga*ODc5MDE2NDY5LjE3NDkxNjkwMjc.*_ga_LXTM6CQ0XK*czE3NDkxNjkwMjckbzEkZzEkdDE3NDkxNjkxNzYkajU0JGwwJGgw*_fplc*UWl6QVF1M3AzRFBnWnNtQXdvRFQlMkJqQXVIN0tRVHYxZzhkWmF6dENUSTN5aWxMc2JYajZ0SXZpb2thNHJLMjRqSWF4NWgwdnRoa1JoMUpiRjhFNHVYOW9hNVVMSnZYMTR1TlJSM2gwQUtURDdXVGJYZEVQVldYQkJFbVRmcEElM0QlM0Q.&_ga=2.42878181.1120551293.1749169027-879016469.1749169027
    name: HubSpot Privacy Policy
    type: PrivacyPolicy
    description: 'null'
  - url: https://www.hubspot.com/our-story
    name: About HubSpot | HubSpot’s Story
    type: About
    description: 'null'
  - url: >-
      https://blog.hubspot.com/?hubs_content=www.hubspot.com/our-story&hubs_content-cta=Blog&_gl=1*1phb45r*_gcl_au*NDQ3NTExOTU2LjE3NDkxNjkxNzA.*FPAU*NDQ3NTExOTU2LjE3NDkxNjkxNzA.*_ga*ODc5MDE2NDY5LjE3NDkxNjkwMjc.*_ga_LXTM6CQ0XK*czE3NDkxNjkwMjckbzEkZzEkdDE3NDkxNjkxOTMkajM3JGwwJGgw*_fplc*UWl6QVF1M3AzRFBnWnNtQXdvRFQlMkJqQXVIN0tRVHYxZzhkWmF6dENUSTN5aWxMc2JYajZ0SXZpb2thNHJLMjRqSWF4NWgwdnRoa1JoMUpiRjhFNHVYOW9hNVVMSnZYMTR1TlJSM2gwQUtURDdXVGJYZEVQVldYQkJFbVRmcEElM0QlM0Q.
    name: HubSpot Blog | Marketing, Sales, Agency, and Customer Success Content
    type: Blog
    description: 'null'
  - url: >-
      https://legal.hubspot.com/security?hubs_content=blog.hubspot.com/&hubs_content-cta=Security&_ga=2.40198370.1120551293.1749169027-879016469.1749169027&_gl=1*17mzhr6*_gcl_au*NDQ3NTExOTU2LjE3NDkxNjkxNzA.*FPAU*NDQ3NTExOTU2LjE3NDkxNjkxNzA.*_ga*ODc5MDE2NDY5LjE3NDkxNjkwMjc.*_ga_LXTM6CQ0XK*czE3NDkxNjkwMjckbzEkZzEkdDE3NDkxNjkyMDMkajI3JGwwJGgw*_fplc*UWl6QVF1M3AzRFBnWnNtQXdvRFQlMkJqQXVIN0tRVHYxZzhkWmF6dENUSTN5aWxMc2JYajZ0SXZpb2thNHJLMjRqSWF4NWgwdnRoa1JoMUpiRjhFNHVYOW9hNVVMSnZYMTR1TlJSM2gwQUtURDdXVGJYZEVQVldYQkJFbVRmcEElM0QlM0Q.
    name: HubSpot Security Program
    type: Security
    description: 'null'
  - url: >-
      https://www.hubspot.com/partners/affiliates?_gl=1*1qccb8u*_gcl_au*NDQ3NTExOTU2LjE3NDkxNjkxNzA.*FPAU*NDQ3NTExOTU2LjE3NDkxNjkxNzA.*_ga*ODc5MDE2NDY5LjE3NDkxNjkwMjc.*_ga_LXTM6CQ0XK*czE3NDkxNjkwMjckbzEkZzEkdDE3NDkxNjkyNjAkajYwJGwwJGgw*_fplc*UWl6QVF1M3AzRFBnWnNtQXdvRFQlMkJqQXVIN0tRVHYxZzhkWmF6dENUSTN5aWxMc2JYajZ0SXZpb2thNHJLMjRqSWF4NWgwdnRoa1JoMUpiRjhFNHVYOW9hNVVMSnZYMTR1TlJSM2gwQUtURDdXVGJYZEVQVldYQkJFbVRmcEElM0QlM0Q.
    name: HubSpot Affiliate Program | Overview
    type: Affiliate
    description: 'null'
  - url: https://www.hubspot.com/partners/affiliates
    name: HubSpot Affiliate Program | Overview
    type: Affiliate
    description: 'null'
  - url: https://www.hubspot.com/partners
    name: HubSpot Partner Programs
    type: Partners
    description: 'null'
  - url: https://www.hubspot.com/pricing/marketing/enterprise
    name: Marketing Software Pricing | HubSpot
    type: Pricing
    description: 'null'
  - url: https://www.hubspot.com/case-studies
    name: Case Studies | HubSpot
    type: CaseStudies
    description: 'null'
  - data:
      - name: Free Meeting Scheduler App
      - name: Email Tracking Software
      - name: AI Content Writer
      - name: AI Website Generator
      - name: Email Marketing Software
      - name: Lead Management Software
      - name: AI Email Writer
      - name: Free Website Builder
      - name: Sales Email Templates
      - name: Free Online Form Builder
      - name: Free Chatbot Builder
      - name: Free Live Chat Software
      - name: Marketing Analytics
      - name: Free Landing Page Builder
      - name: Free Web Hosting
    name: Features
    type: Features
created: 2023/11/14
modified: '2025-06-05'
position: Consuming
description: |-

  HubSpot is a leading CRM platform that provides software and support to help
  businesses grow better. Our platform includes marketing, sales, service, and
  website management products that start free and scale to meet our customers'
  needs at any stage of growth. Today, thousands of customers around the world
  use our powerful and easy-to-use tools and integrations to attract, engage,
  and delight customers.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'

---
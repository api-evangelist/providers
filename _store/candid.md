---
aid: candid
name: Candid
url: https://raw.githubusercontent.com/api-evangelist/candid/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
tags:
  - Charities
  - Donations
  - Non-Profits
  - Philanthropy
  - Foundations
  - Grants
  - 990s
  - Demographics
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-23'
position: Provider
specificationVersion: '0.19'
description: Candid (formed from the 2019 merger of Foundation Center and GuideStar) helps social sector organizations advance their missions by sharing information, breaking down barriers, and improving giving. Candid maintains the most comprehensive set of data on U.S. nonprofits, foundations, grants, and philanthropy, and exposes that data through a family of developer APIs — Essentials, Premier, Charity Check, Demographics, Grants, News, Taxonomy, Eligibility, and PDF/Bulk variants — available through the Candid Developer Portal.
apis:
  - aid: candid:essentials-api
    name: Candid Essentials API
    description: Core nonprofit search and lookup. Provides fast search over Candid's database of U.S. nonprofits by name, EIN, location, NTEE code, size, and more. Returns summary records suitable for autocompletes, lookups, and basic-verification flows. Available in versions v1–v4 with POST and GET variants.
    humanURL: https://developer.candid.org/reference/welcome
    baseURL: https://api.candid.org/essentials
    tags:
      - Nonprofits
      - Search
      - Lookup
    properties:
      - type: Documentation
        url: https://developer.candid.org/reference/welcome
      - type: Portal
        url: https://developer.candid.org/
  - aid: candid:premier-api
    name: Candid Premier API
    description: Deep nonprofit profile data. Returns comprehensive records for a given organization including financials, programs, leadership, board, grants received and awarded, operating details, affiliations, and FTA (Financial Trend Analysis). Supports a Profile PDF generation endpoint for building ready-to-share nonprofit briefs.
    humanURL: https://developer.candid.org/reference/welcome
    baseURL: https://api.candid.org/premier
    tags:
      - Nonprofits
      - Financials
      - Profiles
      - PDF
    properties:
      - type: Documentation
        url: https://developer.candid.org/reference/welcome
      - type: Portal
        url: https://developer.candid.org/
  - aid: candid:charity-check-api
    name: Candid Charity Check API
    description: Real-time nonprofit verification and compliance screening used for due diligence, donation compliance, and tax-deductibility checks. Returns IRS 501(c)(3) status, revocation history, public-charity / private- foundation classification, OFAC watchlist screening, and more. Offers national and state-level endpoints.
    humanURL: https://developer.candid.org/reference/welcome
    baseURL: https://api.candid.org/charitycheck
    tags:
      - Compliance
      - Verification
      - IRS
      - Due Diligence
    properties:
      - type: Documentation
        url: https://developer.candid.org/reference/welcome
      - type: Portal
        url: https://developer.candid.org/
  - aid: candid:demographics-api
    name: Candid Demographics API
    description: Structured demographic data voluntarily provided by nonprofits about their staff, board, and populations served. Enables funders and platforms to analyze equity, diversity, and inclusion across the social sector.
    humanURL: https://developer.candid.org/reference/welcome
    baseURL: https://api.candid.org/demographics
    tags:
      - Demographics
      - DEI
      - Nonprofits
    properties:
      - type: Documentation
        url: https://developer.candid.org/reference/welcome
      - type: Portal
        url: https://developer.candid.org/
  - aid: candid:grants-api
    name: Candid Grants API
    description: Access to Candid's global grants dataset — summary statistics, funders, recipients, and individual transaction records. Useful for philanthropic benchmarking, funder research, and grant-market intelligence.
    humanURL: https://developer.candid.org/reference/welcome
    baseURL: https://api.candid.org/grants
    tags:
      - Grants
      - Funders
      - Recipients
      - Transactions
    properties:
      - type: Documentation
        url: https://developer.candid.org/reference/welcome
      - type: Portal
        url: https://developer.candid.org/
  - aid: candid:news-api
    name: Candid News API
    description: Search and retrieve philanthropic news content from Candid's curated news database covering funders, grantees, sector trends, and policy. Supports customizable parameters for date range, topic, geography, and organization.
    humanURL: https://developer.candid.org/reference/welcome
    baseURL: https://api.candid.org/news
    tags:
      - News
      - Philanthropy
      - Content
    properties:
      - type: Documentation
        url: https://developer.candid.org/reference/welcome
      - type: Portal
        url: https://developer.candid.org/
  - aid: candid:taxonomy-api
    name: Candid Taxonomy API
    description: Returns Candid's philanthropic classification system (subject, population, support-strategy, and geographic area taxonomies) so integrators can consistently tag and query nonprofit, grant, and funder records.
    humanURL: https://developer.candid.org/reference/welcome
    baseURL: https://api.candid.org/taxonomy
    tags:
      - Taxonomy
      - Classification
      - Metadata
    properties:
      - type: Documentation
        url: https://developer.candid.org/reference/welcome
      - type: Portal
        url: https://developer.candid.org/
  - aid: candid:nonprofit-eligibility-api
    name: Candid Nonprofit Eligibility API
    description: Evaluates whether a given nonprofit is eligible to receive a grant or donation based on configurable rules — IRS status, country, OFAC, custom program criteria — to automate grantmaking and giving workflows.
    humanURL: https://developer.candid.org/reference/welcome
    baseURL: https://api.candid.org/eligibility
    tags:
      - Eligibility
      - Grantmaking
      - Compliance
    properties:
      - type: Documentation
        url: https://developer.candid.org/reference/welcome
      - type: Portal
        url: https://developer.candid.org/
common:
  - type: Website
    url: https://candid.org
  - type: DeveloperPortal
    url: https://developer.candid.org/
  - type: DataPortal
    url: https://data.candid.org/reference/welcome-to-candids-data-portal
  - type: APIsOverview
    url: https://candid.org/use-our-data
  - type: PricingAndAccess
    url: https://candid.org/use-our-data
  - type: PrivacyPolicy
    url: https://candid.org/privacy-policy
  - type: TermsOfService
    url: https://candid.org/terms-of-use
  - type: Support
    url: https://help.candid.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

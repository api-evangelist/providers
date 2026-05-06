---
aid: congressional-budget-office
url: https://raw.githubusercontent.com/api-evangelist/congressional-budget-office/refs/heads/main/apis.yml
name: Congressional Budget Office
x-type: government
description: The Congressional Budget Office (CBO) is the U.S. legislative branch agency that provides nonpartisan analyses of budgetary and economic issues to Congress. CBO publishes the Budget and Economic Outlook, projections of spending, revenues, deficits, and debt, cost estimates of legislation, and analytical reports. CBO data is distributed primarily as Excel and PDF files on cbo.gov; CBO does not currently publish a programmatic JSON API, but RSS feeds and downloadable structured workbooks make it possible to ingest CBO data into automated pipelines.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Budget
  - CBO
  - Economic Projections
  - Federal Government
  - Legislative Branch
  - Open Data
  - RSS
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: congressional-budget-office:budget-and-economic-data
    name: CBO Budget and Economic Data
    description: Downloadable budget and economic data accompanying CBO's Budget and Economic Outlook reports. Includes 10-year projections of revenues, outlays, deficits, debt, employment, GDP, interest rates, and historical data going back several decades. Files are published as Excel workbooks and PDFs.
    humanURL: https://www.cbo.gov/data/budget-economic-data
    baseURL: https://www.cbo.gov
    tags:
      - Budget
      - Economic
      - Excel
      - Projections
    properties:
      - type: Documentation
        url: https://www.cbo.gov/data/budget-economic-data
      - type: Reference
        url: https://www.cbo.gov/about/products/budget-economic-data
      - type: Reference
        url: https://www.cbo.gov/data/baseline-projections-selected-programs
    x-features:
      - Budget projections workbook published with each Outlook
      - Historical baseline data extending back to 1962
      - Economic projections including GDP, employment, and rates
      - Excel and PDF formats; no JSON API
    x-useCases:
      - Track CBO baseline revenue and outlay projections over time
      - Compare current law projections with prior CBO baselines
      - Build analytical models that ingest CBO Excel workbooks
  - aid: congressional-budget-office:cost-estimates
    name: CBO Cost Estimates
    description: CBO publishes cost estimates for legislation under consideration by Congress, covering both direct spending and revenue impact and including PAYGO scoring. Cost estimates are released as PDFs along with HTML summaries on cbo.gov.
    humanURL: https://www.cbo.gov/cost-estimates
    baseURL: https://www.cbo.gov
    tags:
      - Cost Estimate
      - Legislation
      - PAYGO
      - Scoring
    properties:
      - type: Documentation
        url: https://www.cbo.gov/cost-estimates
      - type: Reference
        url: https://www.cbo.gov/about/products/ce-faq
      - type: Reference
        url: https://www.cbo.gov/topics/budget
    x-features:
      - Per-bill cost estimate documents indexed on cbo.gov
      - PAYGO scoring summaries
      - Mandatory and discretionary spending breakdowns
      - PDF and HTML; no JSON API
    x-useCases:
      - Track cost estimates of pending legislation
      - Analyze fiscal impact of bills under consideration
      - Build legislative tracking pipelines that link bills to scores
  - aid: congressional-budget-office:publications-rss
    name: CBO Publications RSS Feeds
    description: CBO publishes RSS feeds for its publications, including reports, cost estimates, blog posts, working papers, and presentations. RSS is the primary machine-readable surface for new CBO releases.
    humanURL: https://www.cbo.gov/about/get-cbo-information#rss
    baseURL: https://www.cbo.gov
    tags:
      - Feeds
      - Publications
      - RSS
    properties:
      - type: Documentation
        url: https://www.cbo.gov/about/get-cbo-information#rss
      - type: Reference
        url: https://www.cbo.gov/publications/all/rss.xml
      - type: Reference
        url: https://www.cbo.gov/cost-estimates/rss.xml
    x-features:
      - RSS feeds for publications, cost estimates, and blog
      - Standard RSS 2.0 with title, link, pubDate, and description
      - Polling-friendly machine-readable index of releases
    x-useCases:
      - Notify subscribers of new CBO releases
      - Drive ingestion pipelines for CBO publications
      - Cross-reference RSS items with full publication PDFs
common:
  - type: Website
    url: https://www.cbo.gov/
  - type: Documentation
    url: https://www.cbo.gov/data/budget-economic-data
  - type: Reference
    url: https://www.cbo.gov/about/products
  - type: Feeds
    url: https://www.cbo.gov/about/get-cbo-information#rss
  - type: Privacy Policy
    url: https://www.cbo.gov/about/policies/privacy-and-security-policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

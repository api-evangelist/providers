---
aid: alcohol-and-tobacco-tax-and-trade-bureau
url: https://raw.githubusercontent.com/api-evangelist/alcohol-and-tobacco-tax-and-trade-bureau/refs/heads/main/apis.yml
name: Alcohol and Tobacco Tax and Trade Bureau
tags:
  - Alcohol
  - Tobacco
  - Federal Government
  - Excise Tax
  - Regulation
  - Treasury
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-21T00:00:00.000Z'
modified: '2026-04-19'
position: Consuming
description: The Alcohol and Tobacco Tax and Trade Bureau (TTB), statutorily named the Tax and Trade Bureau, is a bureau of the United States Department of the Treasury. TTB regulates and collects federal excise taxes on alcohol, tobacco, firearms, and ammunition. The bureau enforces Federal laws and regulations related to alcohol and tobacco products, issues permits for producers, importers, and wholesalers, approves label applications for alcohol beverages, and provides open data on tax collections, permit holders, and approved product labels. TTB administers approximately $20 billion in annual federal excise tax collections from the alcohol and tobacco industries.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
apis:
  - aid: alcohol-and-tobacco-tax-and-trade-bureau:ttb-open-data-api
    name: TTB Open Data API
    tags:
      - Open Data
      - Socrata
      - Excise Tax
    humanURL: https://www.ttb.gov/open-government/open-data
    description: The TTB Open Data API provides programmatic access to TTB statistical and regulatory datasets via the Socrata Open Data API (SODA). Available datasets include alcohol beverage tax collections by commodity and state, federal basic permit holders, approved Certificate of Label Approval (COLA) records, and brewery/winery/distillery permit data. The SODA API supports filtering, sorting, pagination, and JSON/CSV output formats.
    properties:
      - type: DataAPI
        url: https://data.ttb.gov/resource/
  - aid: alcohol-and-tobacco-tax-and-trade-bureau:ttb-cola-registry
    name: TTB COLA Registry
    tags:
      - Alcohol Beverage Labels
      - COLA
      - Open Data
    humanURL: https://www.ttb.gov/labeling/cola-registry
    description: The TTB Public COLA (Certificate of Label Approval) Registry provides access to approved alcohol beverage labels. Users and industry members can search for approved labels by product type, brand name, filer name, and approval date. The registry covers wine, distilled spirits, and malt beverage label approvals required before commercial sale in interstate or foreign commerce.
    properties:
      - type: DataAPI
        url: https://www.ttb.gov/labeling/cola-registry
  - aid: alcohol-and-tobacco-tax-and-trade-bureau:ttb-permits-online
    name: TTB Permits Online
    tags:
      - Permits
      - Licensing
      - Alcohol
      - Tobacco
    humanURL: https://www.ttb.gov/permitting/permits-online
    description: TTB Permits Online is the electronic portal for applying for and managing federal basic permits, brewer's notices, distilled spirits plant permits, and tobacco permits. The system allows industry members to submit permit applications, file operational reports, and pay federal excise taxes electronically. Permit status and holder data are published as open data.
    properties:
      - type: GovernmentAPI
        url: https://www.ttb.gov/permitting/permits-online
common:
  - type: Website
    url: https://www.ttb.gov
  - type: Portal
    url: https://www.ttb.gov/open-government/open-data
  - type: DataPortal
    url: https://data.ttb.gov
  - type: Documentation
    url: https://www.ttb.gov/about-ttb/laws-and-regulations
  - type: Contact
    url: https://www.ttb.gov/contact
  - type: PrivacyPolicy
    url: https://www.ttb.gov/about-ttb/privacy-policy
  - type: FOIA
    url: https://www.ttb.gov/about-ttb/foia
  - type: GitHubOrganization
    url: https://github.com/ttb-gov
  - type: Features
    data:
      - name: Excise Tax Data
        description: Annual and monthly federal excise tax collections broken down by alcohol and tobacco commodity type and by state.
      - name: COLA Registry
        description: Public searchable database of all approved Certificate of Label Approval (COLA) records for wine, spirits, and malt beverages.
      - name: Permit Holder Data
        description: Open data on federal basic permit holders including producers, importers, wholesalers, and retailers of alcohol beverages.
      - name: Socrata SODA API
        description: TTB datasets are published on the Socrata platform, accessible via the standard Socrata Open Data API (SODA) with JSON and CSV output.
      - name: Statistical Reports
        description: Annual statistical reports on alcohol and tobacco tax collections, industry production volumes, and commodity statistics.
      - name: eFOIA Portal
        description: Electronic Freedom of Information Act (eFOIA) request submission and tracking for TTB records not available through open data.
  - type: UseCases
    data:
      - name: Alcohol Industry Compliance Research
        description: Producers, importers, and retailers use TTB permit and label data to verify compliance status and competitive market intelligence.
      - name: Tax Revenue Analysis
        description: Policy researchers and economists analyze TTB excise tax collection data to study alcohol and tobacco market trends.
      - name: Label Approval Tracking
        description: Alcohol beverage companies track COLA approval status and research competitor label approvals in the public registry.
      - name: Market Research
        description: Industry analysts use production volume statistics and permit holder counts to assess market size and industry structure.
      - name: Academic Research
        description: Public health researchers use TTB consumption proxy data (tax collection volumes) to study alcohol consumption patterns.
      - name: Journalism and FOIA Research
        description: Journalists and public interest groups use TTB open data and FOIA to investigate regulatory compliance and enforcement actions.
  - type: Integrations
    data:
      - name: api.data.gov
        description: TTB datasets are accessible through api.data.gov, the government-wide API management platform hosted by GSA.
      - name: Data.gov Catalog
        description: TTB open datasets are cataloged on data.gov, the federal open data portal managed by GSA.
      - name: Socrata Open Data Platform
        description: TTB uses the Socrata platform (data.ttb.gov) to publish and provide API access to regulatory datasets.
      - name: IRS
        description: TTB coordinates with the Internal Revenue Service on excise tax administration and data sharing.
      - name: CBP (US Customs)
        description: TTB coordinates with U.S. Customs and Border Protection on alcohol and tobacco import regulation and taxation.
      - name: ATF
        description: TTB works with the Bureau of Alcohol, Tobacco, Firearms and Explosives on shared jurisdiction over alcohol and tobacco regulation.
---

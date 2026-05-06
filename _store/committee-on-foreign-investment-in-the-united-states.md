---
aid: committee-on-foreign-investment-in-the-united-states
url: https://raw.githubusercontent.com/api-evangelist/committee-on-foreign-investment-in-the-united-states/refs/heads/main/apis.yml
name: Committee on Foreign Investment in the United States
x-type: government
description: The Committee on Foreign Investment in the United States (CFIUS) is an inter-agency committee chaired by the U.S. Department of the Treasury that reviews certain foreign investment transactions for national security implications. CFIUS reviews are governed by the Defense Production Act and Section 721, and were significantly strengthened by the Foreign Investment Risk Review Modernization Act of 2018 (FIRRMA). On September 15, 2022, President Biden issued Executive Order 14083 directing CFIUS to focus on emerging national security risks. CFIUS work is largely confidential, and the public-facing surface is limited to regulations, annual reports to Congress, FAQs, declarations and notices guidance, and case studies.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CFIUS
  - Federal Government
  - Foreign Investment
  - National Security
  - Regulation
  - Treasury
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: committee-on-foreign-investment-in-the-united-states:annual-reports
    name: CFIUS Annual Report to Congress
    description: CFIUS publishes an annual report to Congress summarizing covered transactions reviewed during the prior calendar year, statistics on notices, declarations, withdrawn cases, and presidential decisions. Annual reports are released as PDF documents and contain the most complete public statistics on CFIUS activity.
    humanURL: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-reports-and-tables
    baseURL: https://home.treasury.gov
    tags:
      - Annual Report
      - PDF
      - Statistics
      - Transparency
    properties:
      - type: Documentation
        url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-reports-and-tables
      - type: Reference
        url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius
    x-features:
      - Annual aggregate statistics on covered transaction notices
      - Counts of investigations, withdrawals, and presidential actions
      - Industry and country-of-origin breakdowns of reviewed transactions
      - Released as PDF; no machine-readable API or feed
    x-useCases:
      - Researching trends in CFIUS reviews over time
      - Benchmarking national security review activity by sector
      - Informing policy analysis and academic research
  - aid: committee-on-foreign-investment-in-the-united-states:declarations-and-notices
    name: CFIUS Declarations and Notices Guidance
    description: CFIUS provides guidance for parties submitting declarations (short-form filings) and joint voluntary notices (full-form filings) for covered transactions. The Treasury maintains forms, FAQs, and case examples but filings themselves are confidential and are not exposed via any public API.
    humanURL: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-laws-and-guidance
    baseURL: https://home.treasury.gov
    tags:
      - Compliance
      - Declarations
      - Filings
      - Guidance
      - Notices
    properties:
      - type: Documentation
        url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-laws-and-guidance
      - type: Reference
        url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-frequently-asked-questions-faqs
    x-features:
      - Guidance on covered investments under FIRRMA
      - FAQs covering scope, mandatory filings, and timing
      - Forms for declarations and joint voluntary notices
      - Filings are confidential; no public API
    x-useCases:
      - Determining whether a transaction is subject to mandatory filing
      - Preparing declarations or joint voluntary notices
      - Advising clients on CFIUS compliance and timing
  - aid: committee-on-foreign-investment-in-the-united-states:regulations
    name: CFIUS Regulations and Statutes
    description: The CFIUS regulatory framework is published in 31 CFR Parts 800, 801, and 802, and is anchored in Section 721 of the Defense Production Act as amended by FIRRMA. Regulations and statutes are available through the Federal Register, eCFR, and govinfo.gov, all of which expose machine-readable formats such as XML, JSON, and bulk data.
    humanURL: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-laws-and-guidance
    baseURL: https://www.ecfr.gov
    tags:
      - eCFR
      - FIRRMA
      - Federal Register
      - Regulations
      - Statutes
    properties:
      - type: Documentation
        url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-laws-and-guidance
      - type: Reference
        url: https://www.ecfr.gov/current/title-31/subtitle-B/chapter-VIII
      - type: Reference
        url: https://www.federalregister.gov/agencies/foreign-investment-in-the-united-states-office-of-investment-security
    x-features:
      - 31 CFR Parts 800, 801, and 802 cover the CFIUS regulatory regime
      - eCFR provides machine-readable XML and JSON of current regulations
      - Federal Register publishes proposed and final rules with metadata
      - govinfo.gov offers bulk data access to the Code of Federal Regulations
    x-useCases:
      - Tracking changes to CFIUS regulations over time
      - Building tooling that ingests regulatory text from eCFR or govinfo
      - Cross-referencing CFIUS regulations with other federal rules
common:
  - type: Website
    url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius
  - type: Documentation
    url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-laws-and-guidance
  - type: Reference
    url: https://www.ecfr.gov/current/title-31/subtitle-B/chapter-VIII
  - type: Reports
    url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-reports-and-tables
  - type: FAQ
    url: https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-frequently-asked-questions-faqs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

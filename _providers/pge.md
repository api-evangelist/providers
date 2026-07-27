---
api_count: 2
artifact_total: 0
created: '2026-07-27'
description: 'Pacific Gas and Electric Company is the investor-owned electric and natural gas utility for northern and central California — incorporated in California in 1905, headquartered in Oakland, roughly 23,000 employees, a 70,000-square- mile service area, about 5.5 million electric accounts and 4.5 million gas accounts, and a subsidiary of PG&E Corporation. It sits in the wires, pipes and metering layer of the United States value chain: a vertically integrated regulated distribution utility that owns the meter and the customer relationship, does not run the wholesale market (CAISO does), and is regulated by the California Public Utilities Commission. Its API posture is the outlier of the American utility sector and deserves to be recorded precisely, because the United States has no federal energy consumer-data mandate at all. PG&E runs Share My Data, its production Green Button Connect My Data implementation, on a live MuleSoft API gateway at https://api.pge.com — a NAESB REQ.21
  ESPI 1.1 surface with roughly two dozen documented resources under /GreenButtonConnect/espi/1_1/resource/, an OAuth 2.0 authorization server at /datacustodian/oauth/v2/, and a separate published test environment at /datacustodian/test/oauth/v2/. Unlike almost every other US utility, PG&E publishes the whole contract anonymously: a complete supported-API reference, an OAuth/ESPI authorization guide, a relational data model, supported data elements, function-block scope-string mappings, the ESPI and Share My Data XSD schemas, sample MeterReadings XML, Python and JavaScript SDKs with development guides, published rate limits (one request per second per vendor, 2,000 calls per hour and 20,000 calls per 24 hours per client ID) and a SoapUI walkthrough — all reachable without a login at pge.com. What is not open is the data itself. Share My Data is application-approval gated: a third party needs a US EIN, eligible standing with the CPUC, a CA-issued TLS 1.2 X.509 certificate (self-signed rejected),
  acceptance of the CPUC-filed Customer Data Access Tariff, and successful connectivity and OAuth testing before approval, after which every production call runs over mutual TLS with bearer tokens scoped to an individual customer''s authorization. The mandate story is equally specific and must not be flattened into "voluntary Green Button": California compels third-party access through state law and CPUC tariff — Public Utilities Code section 8380 (SB 1476, 2010), the Customer Information Service Request for Share My Data tariff form (Cal. P.U.C. Sheet 55826-E, Sample Form 79-1186, Advice 6900-E, effective 1 April 2023), and Electric Rule 24 / Gas Rule 25 for demand response providers — but no federal obligation and no Ontario-style Green Button regulation applies. The consumer-versus-market split is stark: consumer data is a real, verified, standards-conformant API behind consent and approval, while PG&E publishes no open market or grid API whatsoever. Its aggregated ZIP-code electric and
  gas usage datasets, released quarterly under CPUC Decision 14-05-016 through the Energy Data Request Program, are CSV-in- ZIP downloads behind an organization/name/email form and a data-use agreement, not an anonymous feed; California wholesale market data belongs to CAISO.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: Pacific Gas and Electric
nav: Providers
network: true
random_paper: 44
slug: pge
tags:
- Energy
- United States
- Utilities
- Electricity
- Gas
- California
- Smart Metering
- Green Button
- ESPI
- Energy Data
- Grid
- Demand Response
- Investor-Owned Utility
---

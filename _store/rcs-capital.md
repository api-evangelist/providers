---
aid: rcs-capital
name: RCS Capital
description: RCS Capital Corporation (RCAP) was a publicly traded holding company focused on the financial services industry, founded by Nicholas Schorsch and taken public in June 2013. The firm owned a diversified group of businesses including independent broker-dealers, investment banking, capital markets, and transaction management services. It assembled Cetera Financial Group to become the second largest network of independent broker-dealers in the United States, with approximately 9,100 financial advisors managing $220 billion in assets under administration for 2.5 million clients. RCS Capital filed for Chapter 11 bankruptcy protection in January 2016, citing $1.39 billion in debts, and emerged in May 2016 as Aretec Group, Inc., the holding company of Cetera Financial Group. No public developer APIs were offered under the RCS Capital brand.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/apis.yml
tags:
  - Broker-Dealer
  - Cetera Financial Group
  - Defunct
  - Financial Services
  - Independent Advisor
  - Investment Banking
  - Wealth Management
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    name: RCS Capital SEC Filing Reference
    description: SEC EDGAR filing for RCS Capital Corporation.
    url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001568832&type=&dateb=&owner=include&count=40
  - type: Website
    name: Cetera Financial Group
    description: Successor entity to the Cetera Financial Group businesses assembled by RCS Capital. Cetera continues to operate as a leading network of independent broker-dealers.
    url: https://www.cetera.com
  - type: Documentation
    name: RCS Capital Chapter 11 Case Information
    description: Court-maintained Chapter 11 case documents for RCS Capital restructuring.
    url: https://cases.ra.kroll.com/rcscapital/
  - type: JSONSchema
    name: Financial Advisor Schema
    description: JSON Schema describing a financial advisor profile as used in independent broker-dealer networks.
    url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/json-schema/rcs-capital-financial-advisor-schema.json
  - type: JSONSchema
    name: Broker-Dealer Entity Schema
    description: JSON Schema describing a registered broker-dealer entity.
    url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/json-schema/rcs-capital-broker-dealer-schema.json
  - type: JSONStructure
    name: Financial Advisor Structure
    description: Field-level structure documentation for the financial advisor object.
    url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/json-structure/rcs-capital-financial-advisor-structure.json
  - type: JSONLDContext
    name: RCS Capital JSON-LD Context
    description: JSON-LD context mapping financial services concepts to schema.org and FIBO ontology.
    url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/json-ld/rcs-capital-context.jsonld
  - type: Example
    name: Financial Advisor Example
    description: Example financial advisor record representing the type of data managed within broker-dealer networks.
    url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/examples/rcs-capital-financial-advisor-example.json
  - type: Vocabulary
    name: RCS Capital Vocabulary
    description: Domain vocabulary for independent broker-dealer financial services concepts.
    url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/vocabulary/rcs-capital-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

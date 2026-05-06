---
aid: accounting-standards
url: https://raw.githubusercontent.com/api-evangelist/accounting-standards/refs/heads/main/apis.yml
name: Accounting Standards
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Accounting Standards
  - Finance
  - GAAP
  - IFRS
  - XBRL
  - Financial Reporting
  - SEC
  - FASB
description: Accounting Standards are the formal rules and guidelines that govern how financial transactions and statements are recorded, reported, and disclosed. They ensure consistency, transparency, and comparability across financial reports, and include frameworks like GAAP and IFRS. Digital reporting standards like XBRL enable structured, machine-readable financial filings.
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - name: US GAAP Financial Reporting Taxonomy 2026
    description: The 2026 GAAP Financial Reporting Taxonomy (GRT) is the official XBRL taxonomy maintained by FASB for SEC financial filings. It incorporates updates for FASB accounting standards published through December 1, 2025. The taxonomy provides structured element definitions for US Generally Accepted Accounting Principles (GAAP) financial statement reporting, available in XSD format with namespace http://fasb.org/us-gaap/2026.
    humanURL: https://xbrl.us/xbrl-taxonomy/2026-us-gaap/
    baseURL: https://xbrl.fasb.org/us-gaap/2026/
    tags:
      - GAAP
      - XBRL
      - FASB
      - SEC
      - Financial Reporting
    properties:
      - type: Documentation
        url: https://xbrl.us/xbrl-taxonomy/2026-us-gaap/
      - type: Specification
        url: https://fasb.org/standards
      - type: Documentation
        url: https://asc.fasb.org/
        title: FASB Accounting Standards Codification
  - name: SEC EDGAR XBRL API
    description: The SEC EDGAR XBRL APIs provide free, real-time access to structured financial data from public company filings. APIs include company submissions, company facts (all XBRL disclosures), company concepts (individual taxonomy tags per company), and aggregated XBRL frames across all filers. Data is returned in JSON and covers US-GAAP, IFRS, DEI, and SRT taxonomies. Rate limit is 10 requests/second with required User-Agent header.
    humanURL: https://www.sec.gov/about/developer-resources
    baseURL: https://data.sec.gov/
    tags:
      - SEC
      - EDGAR
      - XBRL
      - Financial Data
      - Open Data
      - REST API
    properties:
      - type: Documentation
        url: https://www.sec.gov/about/developer-resources
      - type: APIReference
        url: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
      - type: RateLimits
        url: https://www.sec.gov/about/developer-resources
        title: 10 requests/second, User-Agent header required
  - name: IFRS Accounting Standards
    description: International Financial Reporting Standards (IFRS) are global accounting standards issued by the International Accounting Standards Board (IASB). IFRS standards govern the financial reporting of companies in over 140 jurisdictions. The IFRS Foundation publishes the IFRS Taxonomy for structured XBRL tagging of IFRS financial statements, referenced by the SEC for foreign private issuers.
    humanURL: https://www.ifrs.org/issued-standards/list-of-standards/
    baseURL: https://www.ifrs.org/
    tags:
      - IFRS
      - IASB
      - International
      - Financial Reporting
      - XBRL
    properties:
      - type: Documentation
        url: https://www.ifrs.org/issued-standards/list-of-standards/
      - type: Specification
        url: https://www.sec.gov/data-research/standard-taxonomies/ifrs-taxonomy
        title: IFRS Taxonomy via SEC
  - name: FASB Accounting Standards Codification
    description: The FASB Accounting Standards Codification (ASC) is the single source of authoritative nongovernmental U.S. GAAP. Organized into Topics, Subtopics, Sections, and Paragraphs, the ASC provides the complete set of accounting guidance for US GAAP. The ASC online provides search, navigation, and research tools for accounting practitioners.
    humanURL: https://asc.fasb.org/
    baseURL: https://asc.fasb.org/
    tags:
      - GAAP
      - FASB
      - Codification
      - US Accounting
    properties:
      - type: Documentation
        url: https://asc.fasb.org/
      - type: Documentation
        url: https://www.fasb.org/standards/accounting-standard-updates
        title: Accounting Standards Updates
  - name: XBRL International Specification
    description: eXtensible Business Reporting Language (XBRL) is an open international standard for digital business reporting maintained by XBRL International. It enables the exchange of business information in a structured, machine-readable format. XBRL is required by the SEC for financial filings and adopted by regulators worldwide including ESMA, EIOPA, and EBA.
    humanURL: https://www.xbrl.org/
    baseURL: https://www.xbrl.org/
    tags:
      - XBRL
      - Digital Reporting
      - Financial Data
      - Open Standard
    properties:
      - type: Documentation
        url: https://www.xbrl.org/
      - type: Specification
        url: https://www.xbrl.org/specification/gnl/rec-2003-12-31/gnl-2003-12-31.htm
        title: XBRL 2.1 Specification
common:
  - type: Website
    url: https://www.fasb.org/
    title: Financial Accounting Standards Board
  - type: Website
    url: https://www.ifrs.org/
    title: IFRS Foundation
  - type: Website
    url: https://xbrl.us/
    title: XBRL US
  - type: GitHubOrganization
    url: https://github.com/xbrl
    title: XBRL GitHub Organization
  - type: Tools
    url: https://data.sec.gov/
    title: SEC EDGAR Data Portal
  - type: Features
    data:
      - name: Structured Financial Reporting
        description: XBRL taxonomies enable machine-readable financial statement reporting that regulators, investors, and analysts can process programmatically.
      - name: US GAAP Codification
        description: The FASB ASC provides the single authoritative source of US GAAP organized by topic for consistent application across entities.
      - name: International Standards Harmonization
        description: IFRS provides globally harmonized accounting standards enabling cross-border financial comparability in over 140 jurisdictions.
      - name: Real-Time Financial Data Access
        description: SEC EDGAR XBRL APIs provide real-time access to structured financial data from all public company filings as JSON.
      - name: Data Quality Rules
        description: The Data Quality Committee Rules Taxonomy (DQCRT) provides machine-enforceable rules for validating XBRL-tagged financial data.
      - name: Taxonomy Versioning
        description: Annual FASB taxonomy releases incorporate new accounting standards and ensure accurate representation of current GAAP requirements.
  - type: UseCases
    data:
      - name: Public Company Financial Reporting
        description: Companies use XBRL taxonomies when filing 10-K, 10-Q, and 8-K reports with the SEC, ensuring structured, machine-readable disclosure.
      - name: Financial Data Analysis
        description: Investors and analysts use SEC EDGAR XBRL APIs to retrieve structured financial statements for quantitative analysis and screening.
      - name: Accounting Research
        description: CPAs and finance professionals use the FASB ASC to research applicable US GAAP guidance for specific transaction types and disclosures.
      - name: Regulatory Compliance
        description: Finance teams implement GAAP or IFRS accounting standards to meet regulatory requirements and auditor expectations.
      - name: FinTech Integration
        description: FinTech platforms integrate with SEC EDGAR APIs to ingest standardized financial data for valuation models, credit analysis, and benchmarking.
  - type: Integrations
    data:
      - name: SEC EDGAR
        description: The SEC's public filing database mandating XBRL for financial disclosures, providing free API access to all structured filing data.
      - name: XBRL US
        description: Industry consortium supporting XBRL adoption in the US, providing taxonomy resources, training, and data quality rule development.
      - name: iXBRL (Inline XBRL)
        description: Human-readable HTML combining with machine-readable XBRL tags, now required by the SEC for financial statement filings.
      - name: ESMA / European Reporting
        description: European Securities and Markets Authority mandating IFRS XBRL reporting under the European Single Electronic Format (ESEF).
      - name: Deloitte DART
        description: Deloitte's Accounting Research Tool providing access to FASB ASC and IFRS standards with interpretive guidance and examples.
  - type: JSON-LD
    url: https://raw.githubusercontent.com/api-evangelist/accounting-standards/refs/heads/main/json-ld/accounting-standards-context.jsonld
    title: Accounting Standards JSON-LD Context
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/accounting-standards/refs/heads/main/vocabulary/accounting-standards-vocabulary.yaml
    title: Accounting Standards Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

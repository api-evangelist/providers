---
aid: bloom-credit
url: https://raw.githubusercontent.com/api-evangelist/bloom-credit/refs/heads/main/apis.yml
name: Bloom Credit
description: Bloom Credit is a fintech infrastructure company providing API access to consumer credit data from all three major credit bureaus (Equifax, Experian, TransUnion). The platform enables fintechs, lenders, and financial services applications to retrieve credit reports, credit scores, trade line data, and enroll consumers in real-time credit monitoring. Bloom Credit provides multi-language SDKs (Python, Ruby, TypeScript, R, Go) and supports the Metro 2 credit reporting format.
tags:
  - Credit Bureau
  - Credit Reports
  - Credit Scores
  - Fintech
  - Lending
  - Personal Finance
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-24'
modified: '2026-04-19'
position: Consuming
specificationVersion: '0.19'
apis:
  - aid: bloom-credit:bloom-credit-api
    name: Bloom Credit API
    description: RESTful API providing access to consumer credit data from Equifax, Experian, and TransUnion. Supports consumer registration with consent, tri-bureau credit report retrieval, FICO and VantageScore credit scores, trade line data, and real-time credit monitoring with webhook alerts. Requires API key authentication.
    humanURL: https://bloomcredit.io/
    tags:
      - Credit Bureau
      - Credit Reports
      - Credit Scores
      - Fintech
      - Lending
    properties:
      - type: Documentation
        url: https://bloomcredit.io/
      - type: OpenAPI
        url: openapi/bloom-credit-api-openapi.yaml
      - type: NaftikoCapability
        url: capabilities/bloom-credit-credit-intelligence.yaml
      - type: SpectralRules
        url: rules/bloom-credit-spectral-rules.yml
      - type: Vocabulary
        url: vocabulary/bloom-credit-vocabulary.yaml
common:
  - type: Website
    url: https://bloomcredit.io/
  - type: Documentation
    url: https://bloomcredit.io/
  - type: GettingStarted
    url: https://bloomcredit.io/
  - type: GitHubOrganization
    url: https://github.com/bloomcredit
  - type: SDK
    url: https://github.com/bloomcredit/bloomPy
    title: Python SDK
  - type: SDK
    url: https://github.com/bloomcredit/bloomTypescript
    title: TypeScript SDK
  - type: TermsOfService
    url: https://bloomcredit.io/terms
  - type: PrivacyPolicy
    url: https://bloomcredit.io/privacy
  - type: SpectralRules
    url: rules/bloom-credit-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/bloom-credit-credit-intelligence.yaml
  - type: Vocabulary
    url: vocabulary/bloom-credit-vocabulary.yaml
  - type: Features
    data:
      - name: Tri-Bureau Credit Reports
        description: Pull full credit reports from Equifax, Experian, and TransUnion in a single API call with structured trade line, inquiry, and public record data.
      - name: Credit Score Retrieval
        description: Access FICO 8, VantageScore 3.0, and other scoring models from all three major credit bureaus for comprehensive creditworthiness assessment.
      - name: Trade Line Data
        description: Retrieve individual account and trade line records including payment history, balances, credit limits, and account status across bureaus.
      - name: Real-Time Credit Monitoring
        description: Enroll consumers in monitoring subscriptions that trigger webhook alerts for new accounts, inquiries, derogatory marks, and score changes.
      - name: Consumer Consent Management
        description: Built-in consumer registration and consent workflow ensuring FCRA-compliant access to credit bureau data with auditable consent records.
      - name: Multi-Language SDKs
        description: Official SDKs for Python, TypeScript, Ruby, R, and Go enabling rapid integration into existing fintech and data science workflows.
  - type: UseCases
    data:
      - name: Loan Underwriting
        description: Lenders pull tri-bureau credit reports and scores during loan origination to assess creditworthiness and determine loan terms.
      - name: Credit Building Apps
        description: Consumer fintech applications provide users with free credit score monitoring and personalized recommendations to improve their credit profiles.
      - name: Tenant Screening
        description: Property management platforms use Bloom Credit to run credit checks during rental application processing.
      - name: Credit Counseling
        description: Financial advisors and credit counselors access full credit reports and trade line data to create personalized debt management plans.
      - name: Account Origination
        description: Financial institutions use credit data during account opening to verify identity and assess risk for credit card and deposit products.
  - type: Integrations
    data:
      - name: Equifax
        description: Direct integration with Equifax for credit report and score data including FICO 8 and other proprietary scoring models.
      - name: Experian
        description: Direct integration with Experian for credit reports, FICO scores, and VantageScore data with real-time data freshness.
      - name: TransUnion
        description: Direct integration with TransUnion for credit reports and scores with support for TransUnion-specific data attributes.
      - name: Plaid
        description: Complementary integration where Bloom Credit's credit data can be combined with Plaid's bank account and income verification for full financial profiles.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

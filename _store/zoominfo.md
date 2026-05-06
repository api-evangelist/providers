---
aid: zoominfo
url: https://raw.githubusercontent.com/api-evangelist/zoominfo/refs/heads/main/apis.yml
apis:
  - aid: zoominfo:zoominfo
    name: ZoomInfo
    tags:
      - Authentication
      - Contact Search
      - Company Search
      - Contact Enrich
      - Company Enrich
      - Intent Search
      - News Search
      - Scoop Search
      - Technology Enrich
      - Webhooks
      - Bulk Operations
      - WebSights
      - Compliance
      - Lookup
      - Corporate Hierarchy
      - Org Chart
    humanURL: https://www.zoominfo.com/
    properties:
      - url: https://www.zoominfo.com/solutions/data-as-a-service/enterprise-api
        type: Documentation
      - type: OpenAPI
        url: openapi/zoominfo-openapi.yml
      - type: SDK
        url: https://github.com/Zoominfo/api-auth-python-client
        title: Python SDK
      - type: SDK
        url: https://github.com/Zoominfo/api-auth-java-client
        title: Java SDK
      - type: SDK
        url: https://github.com/Zoominfo/api-auth-nodejs-client
        title: Node.js SDK
      - type: SDK
        url: https://github.com/Zoominfo/api-auth-csharp-client
        title: C# SDK
      - type: JSONSchema
        url: json-schema/zoominfo-address-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-authenticate-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-bulk-company-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-bulk-company-search-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-bulk-contact-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-bulk-contact-search-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-bulk-job-results-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-bulk-job-status-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-company-enrich-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-company-enrich-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-company-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-company-funding-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-company-master-data-enrich-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-company-master-data-enrich-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-company-master-data-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-company-search-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-company-search-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-competitor-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-compliance-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-contact-enrich-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-contact-enrich-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-contact-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-contact-search-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-contact-search-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-contact-search-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-corporate-hierarchy-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-create-webhook-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-description-list-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-education-degree-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-education-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-employment-history-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-external-url-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-family-tree-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-get-company-ranking-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-get-company-search-output-field-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-get-corporate-hierarchy-enrich-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-get-corporate-hierarchy-enrich-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-get-hashtag-enrich-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-get-location-enrich-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-get-technology-enrich-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-hashtag-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-hashtags-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-i-p-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-intent-enrich-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-intent-enrich-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-intent-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-intent-search-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-intent-search-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-intent-search-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-intent-topic-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-location-enrich-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-location-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-location-match-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-match-company-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-match-person-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-match-reason-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-naics-code-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-news-enrich-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-news-enrich-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-news-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-news-search-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-news-search-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-news-search-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-org-chart-enrich-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-org-chart-enrich-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-org-chart-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-recommended-contact-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-scoop-enrich-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-scoop-enrich-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-scoop-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-scoop-search-input-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-scoop-search-output-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-scoop-search-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-sic-code-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-social-media-url-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-sub-unit-type-info-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-subscription-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-tech-attribute-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-technology-enrich-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-type-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-update-webhook-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-usage-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-validate-target-u-r-l-request-schema.json
      - type: JSONSchema
        url: json-schema/zoominfo-webhook-schema.json
      - type: JSONStructure
        url: json-structure/zoominfo-address-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-authenticate-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-bulk-company-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-bulk-company-search-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-bulk-contact-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-bulk-contact-search-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-bulk-job-results-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-bulk-job-status-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-company-enrich-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-company-enrich-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-company-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-company-funding-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-company-master-data-enrich-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-company-master-data-enrich-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-company-master-data-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-company-search-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-company-search-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-competitor-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-compliance-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-contact-enrich-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-contact-enrich-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-contact-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-contact-search-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-contact-search-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-contact-search-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-corporate-hierarchy-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-create-webhook-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-description-list-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-education-degree-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-education-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-employment-history-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-external-url-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-family-tree-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-get-company-ranking-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-get-company-search-output-field-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-get-corporate-hierarchy-enrich-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-get-corporate-hierarchy-enrich-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-get-hashtag-enrich-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-get-location-enrich-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-get-technology-enrich-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-hashtag-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-hashtags-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-i-p-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-intent-enrich-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-intent-enrich-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-intent-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-intent-search-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-intent-search-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-intent-search-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-intent-topic-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-location-enrich-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-location-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-location-match-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-match-company-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-match-person-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-match-reason-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-naics-code-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-news-enrich-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-news-enrich-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-news-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-news-search-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-news-search-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-news-search-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-org-chart-enrich-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-org-chart-enrich-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-org-chart-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-recommended-contact-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-scoop-enrich-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-scoop-enrich-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-scoop-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-scoop-search-input-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-scoop-search-output-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-scoop-search-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-sic-code-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-social-media-url-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-sub-unit-type-info-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-subscription-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-tech-attribute-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-technology-enrich-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-type-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-update-webhook-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-usage-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-validate-target-u-r-l-request-structure.json
      - type: JSONStructure
        url: json-structure/zoominfo-webhook-structure.json
      - type: JSONLD
        url: json-ld/zoominfo-context.jsonld
      - type: Example
        url: examples/zoominfo-address-example.json
      - type: Example
        url: examples/zoominfo-authenticate-request-example.json
      - type: Example
        url: examples/zoominfo-bulk-company-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-bulk-company-search-request-example.json
      - type: Example
        url: examples/zoominfo-bulk-contact-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-bulk-contact-search-request-example.json
      - type: Example
        url: examples/zoominfo-bulk-job-results-request-example.json
      - type: Example
        url: examples/zoominfo-bulk-job-status-request-example.json
      - type: Example
        url: examples/zoominfo-company-enrich-input-example.json
      - type: Example
        url: examples/zoominfo-company-enrich-output-example.json
      - type: Example
        url: examples/zoominfo-company-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-company-funding-example.json
      - type: Example
        url: examples/zoominfo-company-master-data-enrich-input-example.json
      - type: Example
        url: examples/zoominfo-company-master-data-enrich-output-example.json
      - type: Example
        url: examples/zoominfo-company-master-data-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-company-search-input-example.json
      - type: Example
        url: examples/zoominfo-company-search-request-example.json
      - type: Example
        url: examples/zoominfo-competitor-example.json
      - type: Example
        url: examples/zoominfo-compliance-output-example.json
      - type: Example
        url: examples/zoominfo-contact-enrich-input-example.json
      - type: Example
        url: examples/zoominfo-contact-enrich-output-example.json
      - type: Example
        url: examples/zoominfo-contact-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-contact-search-input-example.json
      - type: Example
        url: examples/zoominfo-contact-search-output-example.json
      - type: Example
        url: examples/zoominfo-contact-search-request-example.json
      - type: Example
        url: examples/zoominfo-corporate-hierarchy-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-create-webhook-request-example.json
      - type: Example
        url: examples/zoominfo-description-list-example.json
      - type: Example
        url: examples/zoominfo-education-degree-example.json
      - type: Example
        url: examples/zoominfo-education-example.json
      - type: Example
        url: examples/zoominfo-employment-history-example.json
      - type: Example
        url: examples/zoominfo-external-url-example.json
      - type: Example
        url: examples/zoominfo-family-tree-example.json
      - type: Example
        url: examples/zoominfo-get-company-ranking-example.json
      - type: Example
        url: examples/zoominfo-get-company-search-output-field-example.json
      - type: Example
        url: examples/zoominfo-get-corporate-hierarchy-enrich-input-example.json
      - type: Example
        url: examples/zoominfo-get-corporate-hierarchy-enrich-output-example.json
      - type: Example
        url: examples/zoominfo-get-hashtag-enrich-input-example.json
      - type: Example
        url: examples/zoominfo-get-location-enrich-input-example.json
      - type: Example
        url: examples/zoominfo-get-technology-enrich-input-example.json
      - type: Example
        url: examples/zoominfo-hashtag-example.json
      - type: Example
        url: examples/zoominfo-hashtags-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-i-p-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-intent-enrich-input-example.json
      - type: Example
        url: examples/zoominfo-intent-enrich-output-example.json
      - type: Example
        url: examples/zoominfo-intent-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-intent-search-input-example.json
      - type: Example
        url: examples/zoominfo-intent-search-output-example.json
      - type: Example
        url: examples/zoominfo-intent-search-request-example.json
      - type: Example
        url: examples/zoominfo-intent-topic-example.json
      - type: Example
        url: examples/zoominfo-location-enrich-output-example.json
      - type: Example
        url: examples/zoominfo-location-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-location-match-example.json
      - type: Example
        url: examples/zoominfo-match-company-input-example.json
      - type: Example
        url: examples/zoominfo-match-person-input-example.json
      - type: Example
        url: examples/zoominfo-match-reason-example.json
      - type: Example
        url: examples/zoominfo-naics-code-example.json
      - type: Example
        url: examples/zoominfo-news-enrich-input-example.json
      - type: Example
        url: examples/zoominfo-news-enrich-output-example.json
      - type: Example
        url: examples/zoominfo-news-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-news-search-input-example.json
      - type: Example
        url: examples/zoominfo-news-search-output-example.json
      - type: Example
        url: examples/zoominfo-news-search-request-example.json
      - type: Example
        url: examples/zoominfo-org-chart-enrich-input-example.json
      - type: Example
        url: examples/zoominfo-org-chart-enrich-output-example.json
      - type: Example
        url: examples/zoominfo-org-chart-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-recommended-contact-example.json
      - type: Example
        url: examples/zoominfo-scoop-enrich-input-example.json
      - type: Example
        url: examples/zoominfo-scoop-enrich-output-example.json
      - type: Example
        url: examples/zoominfo-scoop-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-scoop-search-input-example.json
      - type: Example
        url: examples/zoominfo-scoop-search-output-example.json
      - type: Example
        url: examples/zoominfo-scoop-search-request-example.json
      - type: Example
        url: examples/zoominfo-sic-code-example.json
      - type: Example
        url: examples/zoominfo-social-media-url-example.json
      - type: Example
        url: examples/zoominfo-sub-unit-type-info-example.json
      - type: Example
        url: examples/zoominfo-subscription-example.json
      - type: Example
        url: examples/zoominfo-tech-attribute-example.json
      - type: Example
        url: examples/zoominfo-technology-enrich-request-example.json
      - type: Example
        url: examples/zoominfo-type-example.json
      - type: Example
        url: examples/zoominfo-update-webhook-request-example.json
      - type: Example
        url: examples/zoominfo-usage-example.json
      - type: Example
        url: examples/zoominfo-validate-target-u-r-l-request-example.json
      - type: Example
        url: examples/zoominfo-webhook-example.json
    description: The ZoomInfo API is a set of HTTPS endpoints you can use to programmatically retrieve and integrate ZoomInfo data into your existing technology stack and ...
name: ZoomInfo
tags:
  - B2B
  - B2B Data
  - Company Data
  - Contact Database
  - Contacts
  - Data
  - Lead Generation
  - Marketing Intelligence
  - Sales Intelligence
type: Contract
image: https://www.zoominfo.com/assets/img/zoominfo-logo.png
access: 3rd-Party
common:
  - url: https://www.zoominfo.com/pricing
    name: Pricing | ZoomInfo
    type: Pricing
  - url: https://pipeline.zoominfo.com/
    name: B2B Sales and Marketing Content | ZoomInfo Blog
    type: Blog
  - url: https://www.zoominfo.com/about/case-studies
    name: Case Studies | Customer Success | ZoomInfo
    type: Customers
  - url: https://www.zoominfo.com/partner
    name: Program Partnership Benefits | Partner with ZoomInfo
    type: Partners
  - url: https://www.zoominfo.com/about/help-center
    name: Help Center | ZoomInfo
    type: Support
  - url: https://www.zoominfo.com/faqs/business
    name: Frequently Asked Questions About ZoomInfos Business
    type: FAQ
  - url: https://pipeline.zoominfo.com/glossary
    name: Go-to-Market Glossary | ZoomInfo Blog
    type: Glossary
  - url: https://api-docs.zoominfo.com/#authentication
    type: Authentication
  - url: https://api-docs.zoominfo.com/getting-started
    type: GettingStarted
  - url: https://api-docs.zoominfo.com/rate-limits
    type: RateLimits
  - url: https://www.zoominfo.com/about/terms-of-service
    type: TermsOfService
  - url: https://www.zoominfo.com/about/privacy-policy
    type: PrivacyPolicy
  - url: https://status.zoominfo.com
    type: StatusPage
  - type: Features
    data:
      - name: Contact Search
        description: Search for contacts by job title, company, location, industry, and other criteria
      - name: Company Search
        description: Search for companies by industry, revenue, employee count, location, and technology stack
      - name: Contact Enrichment
        description: Enrich contact records with verified email addresses, phone numbers, and professional details
      - name: Company Enrichment
        description: Enrich company records with firmographic data including revenue, employee count, and technographics
      - name: Intent Data
        description: Identify companies showing buying intent signals based on content consumption patterns
      - name: Scoops
        description: Access business intelligence scoops about company changes, hiring, and strategic initiatives
      - name: News Intelligence
        description: Search and enrich news articles related to companies and contacts
      - name: Technology Tracking
        description: Identify technologies used by companies across their tech stack
      - name: Corporate Hierarchy
        description: Map organizational structures including parent companies, subsidiaries, and divisions
      - name: Org Chart
        description: Access organizational chart data showing reporting relationships within companies
      - name: Webhooks
        description: Real-time notifications for data changes and updates via webhook subscriptions
      - name: Bulk Operations
        description: Submit batch search and enrichment jobs for large-scale data processing
      - name: WebSights
        description: Identify website visitors by IP address and enrich with company information
      - name: Compliance
        description: Access compliance data to support GDPR and privacy regulation requirements
  - type: UseCases
    data:
      - name: Sales Prospecting
        description: Identify and prioritize ideal prospects using firmographic and intent data to build targeted sales pipelines
      - name: Lead Enrichment
        description: Automatically enrich inbound leads with verified contact and company data for faster qualification
      - name: Account-Based Marketing
        description: Build targeted account lists and personalize outreach using detailed company intelligence
      - name: CRM Data Hygiene
        description: Cleanse and update CRM records with accurate contact information and company details
      - name: Market Research
        description: Analyze market segments, technology adoption, and competitive landscapes using company data
      - name: Competitive Intelligence
        description: Monitor competitor activities, technology changes, and strategic moves through scoops and news
      - name: Buyer Intent Analysis
        description: Identify accounts actively researching solutions in your category based on intent signals
      - name: Website Visitor Identification
        description: Convert anonymous website traffic into identified company accounts using IP enrichment
  - type: Integrations
    data:
      - name: Salesforce
        description: Native integration to enrich and sync contact and company data with Salesforce CRM
      - name: HubSpot
        description: Seamless integration to push enriched data into HubSpot CRM and marketing automation
      - name: Microsoft Dynamics 365
        description: Integration to enrich records and sync data with Microsoft Dynamics CRM
      - name: Marketo
        description: Marketing automation integration for lead enrichment and scoring with Marketo
      - name: Outreach
        description: Sales engagement platform integration for enriched prospect data in Outreach sequences
      - name: Salesloft
        description: Integration to power Salesloft cadences with verified contact information
      - name: Slack
        description: Notifications and alerts for intent signals and data updates delivered to Slack channels
      - name: Snowflake
        description: Data sharing integration to access ZoomInfo data directly in Snowflake data warehouse
      - name: Google Ads
        description: Audience targeting integration to reach ideal prospects with Google advertising campaigns
      - name: LinkedIn
        description: Integration to match and enrich LinkedIn profile data with ZoomInfo intelligence
  - type: GitHubOrganization
    url: https://github.com/Zoominfo
  - type: DeveloperPortal
    url: https://api-docs.zoominfo.com
  - type: APIReference
    url: https://api-docs.zoominfo.com
  - type: Hub
    url: https://github.com/Zoominfo/zoominfo-mcp-plugin
    title: MCP Server
  - type: SpectralRules
    url: rules/zoominfo-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/zoominfo-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/data-enrichment.yaml
  - type: NaftikoCapability
    url: capabilities/sales-prospecting.yaml
  - type: NaftikoCapability
    url: capabilities/shared/zoominfo-api.yaml
created: '2025-02-09'
modified: '2026-04-18'
position: Consuming
description: ZoomInfo is a leading B2B contact database and sales intelligence platform that provides detailed company and contact information, helping sales and marketing teams identify and connect with potential customers.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---

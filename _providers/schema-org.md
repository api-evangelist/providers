---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: 'Schema.org is a collaborative, community-driven vocabulary for structured data on the internet. It provides a collection of shared vocabularies that webmasters and developers can use to mark up pages '
  name: Schema.org Vocabulary
  slug: schemaorg-vocabulary
- description: The Schema.org JSON-LD Context provides the canonical JSON-LD context file for the Schema.org vocabulary. This context file maps Schema.org terms to their full IRIs, enabling JSON-LD processors to cor
  name: Schema.org JSON-LD Context
  slug: schemaorg-json-ld-context
- description: 'The Schema.org Markup Validator tests and validates structured data markup against the Schema.org vocabulary. It supports JSON-LD, Microdata, and RDFa formats and helps ensure structured data will be '
  name: Schema.org Markup Validator
  slug: schemaorg-markup-validator
- description: The Schema.org WebAPI type defines a Web API accessible over Web and Internet technologies. It provides standardized properties for describing APIs including documentation URL, terms of service, provi
  name: Schema.org WebAPI Type
  slug: schemaorg-webapi-type
artifact_total: 93
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/schemaorg/schemaorg/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/schemaorg/schemaorg/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/schema-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://schema.org/
- group: docs
  title: ''
  type: Documentation
  url: https://schema.org/docs/documents.html
- group: company
  title: ''
  type: Blog
  url: https://blog.schema.org/
- group: operate
  title: ''
  type: Support
  url: https://github.com/schemaorg/schemaorg/issues
- group: design
  title: ''
  type: SpectralRules
  url: rules/schema-org-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/schema-org-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/schema-org-vocabulary.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://schema.org/docs/developers.html
- group: start
  title: ''
  type: GettingStarted
  url: https://schema.org/docs/gs.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/schemaorg
- group: commercial
  title: ''
  type: TermsOfService
  url: https://schema.org/docs/terms.html
- group: build
  title: ''
  type: Packages
  url: packages/schema-org-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/schema-org-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/schema-org-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/schema-org-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/schema-org-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/schema-org-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/schema-org-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/schema-org-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/schema-org-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/schema-org-rate-limits.yml
created: '2026-05-02'
description: Schema.org is a collaborative, community-driven project that creates and maintains a shared vocabulary for structured data on the web. Founded by Google, Microsoft, Yahoo, and Yandex in 2011, it provides types and properties that developers and webmasters use to annotate content in formats like JSON-LD, RDFa, and Microdata, enabling search engines and applications to better understand web content. The vocabulary currently consists of 800+ Types, 1500+ Properties, and covers domains including commerce, healthcare, organizations, events, creative works, and more. The Schema.org WebAPI type provides a standardized vocabulary for describing APIs in structured data.
examples:
- key_count: 3
  name: Schema Org Product Example
  slug: schema-org-product-example
- key_count: 3
  name: Schema Org Web Api Example
  slug: schema-org-web-api-example
finops:
- name: Schema Org Finops
  service_category: API
  slug: schema-org-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/schema-org.png
json_schemas:
- name: Schema.org Action
  property_count: 17
  slug: schema-org-action
- name: Schema.org AggregateRating
  property_count: 8
  slug: schema-org-aggregate-rating
- name: Schema.org Article
  property_count: 26
  slug: schema-org-article
- name: Schema.org BlogPosting
  property_count: 20
  slug: schema-org-blog-posting
- name: Schema.org Book
  property_count: 21
  slug: schema-org-book
- name: Schema.org BreadcrumbList
  property_count: 6
  slug: schema-org-breadcrumb-list
- name: Schema.org ContactPoint
  property_count: 13
  slug: schema-org-contact-point
- name: Schema.org Course
  property_count: 23
  slug: schema-org-course
- name: Schema.org CreativeWork
  property_count: 41
  slug: schema-org-creative-work
- name: Schema.org Drug
  property_count: 31
  slug: schema-org-drug
- name: Schema.org Event
  property_count: 30
  slug: schema-org-event
- name: Schema.org FAQPage
  property_count: 12
  slug: schema-org-faq-page
- name: Schema.org GeoCoordinates
  property_count: 8
  slug: schema-org-geo-coordinates
- name: Schema.org HowTo
  property_count: 18
  slug: schema-org-how-to
- name: Schema.org ImageObject
  property_count: 22
  slug: schema-org-image-object
- name: Schema.org Invoice
  property_count: 18
  slug: schema-org-invoice
- name: Schema.org ItemList
  property_count: 8
  slug: schema-org-item-list
- name: Schema.org JobPosting
  property_count: 26
  slug: schema-org-job-posting
- name: Schema.org LocalBusiness
  property_count: 29
  slug: schema-org-local-business
- name: Schema.org MediaObject
  property_count: 20
  slug: schema-org-media-object
- name: Schema.org MedicalCondition
  property_count: 21
  slug: schema-org-medical-condition
- name: Schema.org MedicalProcedure
  property_count: 19
  slug: schema-org-medical-procedure
- name: Schema.org Offer
  property_count: 31
  slug: schema-org-offer
- name: Schema.org Order
  property_count: 22
  slug: schema-org-order
- name: Schema.org Organization
  property_count: 33
  slug: schema-org-organization
- name: Schema.org Person
  property_count: 31
  slug: schema-org-person
- name: Schema.org Place
  property_count: 26
  slug: schema-org-place
- name: Schema.org PostalAddress
  property_count: 15
  slug: schema-org-postal-address
- name: Schema.org Product
  property_count: 35
  slug: schema-org-product
- name: Schema.org PropertyValue
  property_count: 12
  slug: schema-org-property-value
- name: Schema.org QuantitativeValue
  property_count: 10
  slug: schema-org-quantitative-value
- name: Schema.org Review
  property_count: 15
  slug: schema-org-review
- name: Schema.org SearchAction
  property_count: 9
  slug: schema-org-search-action
- name: Schema.org Service
  property_count: 24
  slug: schema-org-service
- name: Schema.org SoftwareApplication
  property_count: 31
  slug: schema-org-software-application
- name: Schema.org Thing
  property_count: 13
  slug: schema-org-thing
- name: Schema.org VideoObject
  property_count: 27
  slug: schema-org-video-object
- name: Schema.org WebAPI
  property_count: 12
  slug: schema-org-web-api
- name: Schema.org WebPage
  property_count: 22
  slug: schema-org-web-page
- name: Schema.org WebSite
  property_count: 11
  slug: schema-org-web-site
json_structures:
- name: Schema Org Action
  property_count: 17
  slug: schema-org-action
- name: Schema Org Aggregate Rating
  property_count: 8
  slug: schema-org-aggregate-rating
- name: Schema Org Article
  property_count: 26
  slug: schema-org-article
- name: Schema Org Blog Posting
  property_count: 19
  slug: schema-org-blog-posting
- name: Schema Org Book
  property_count: 21
  slug: schema-org-book
- name: Schema Org Breadcrumb List
  property_count: 6
  slug: schema-org-breadcrumb-list
- name: Schema Org Contact Point
  property_count: 13
  slug: schema-org-contact-point
- name: Schema Org Course
  property_count: 23
  slug: schema-org-course
- name: Schema Org Creative Work
  property_count: 39
  slug: schema-org-creative-work
- name: Schema Org Drug
  property_count: 30
  slug: schema-org-drug
- name: Schema Org Event
  property_count: 30
  slug: schema-org-event
- name: Schema Org Faq Page
  property_count: 12
  slug: schema-org-faq-page
- name: Schema Org Geo Coordinates
  property_count: 8
  slug: schema-org-geo-coordinates
- name: Schema Org How To
  property_count: 18
  slug: schema-org-how-to
- name: Schema Org Image Object
  property_count: 22
  slug: schema-org-image-object
- name: Schema Org Invoice
  property_count: 18
  slug: schema-org-invoice
- name: Schema Org Item List
  property_count: 8
  slug: schema-org-item-list
- name: Schema Org Job Posting
  property_count: 25
  slug: schema-org-job-posting
- name: Schema Org Local Business
  property_count: 29
  slug: schema-org-local-business
- name: Schema Org Media Object
  property_count: 20
  slug: schema-org-media-object
- name: Schema Org Medical Condition
  property_count: 21
  slug: schema-org-medical-condition
- name: Schema Org Medical Procedure
  property_count: 17
  slug: schema-org-medical-procedure
- name: Schema Org Offer
  property_count: 30
  slug: schema-org-offer
- name: Schema Org Order
  property_count: 22
  slug: schema-org-order
- name: Schema Org Organization
  property_count: 33
  slug: schema-org-organization
- name: Schema Org Person
  property_count: 31
  slug: schema-org-person
- name: Schema Org Place
  property_count: 26
  slug: schema-org-place
- name: Schema Org Postal Address
  property_count: 15
  slug: schema-org-postal-address
- name: Schema Org Product
  property_count: 35
  slug: schema-org-product
- name: Schema Org Property Value
  property_count: 11
  slug: schema-org-property-value
- name: Schema Org Quantitative Value
  property_count: 9
  slug: schema-org-quantitative-value
- name: Schema Org Review
  property_count: 15
  slug: schema-org-review
- name: Schema Org Search Action
  property_count: 9
  slug: schema-org-search-action
- name: Schema Org Service
  property_count: 20
  slug: schema-org-service
- name: Schema Org Software Application
  property_count: 30
  slug: schema-org-software-application
- name: Schema Org Thing
  property_count: 13
  slug: schema-org-thing
- name: Schema Org Video Object
  property_count: 27
  slug: schema-org-video-object
- name: Schema Org Web Api
  property_count: 12
  slug: schema-org-web-api
- name: Schema Org Web Page
  property_count: 21
  slug: schema-org-web-page
- name: Schema Org Web Site
  property_count: 11
  slug: schema-org-web-site
jsonld:
- class_count: 0
  name: Schema Org Context
  property_count: 8
  slug: schema-org-context
layout: provider
modified: '2026-08-13'
name: Schema.org
nav: Providers
network: true
overview: 'Schema.org publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Schema.org, Structured Data, Linked Data, JSON-LD, and Vocabulary.


  The Schema.org catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Schema.org''s developer surface includes documentation, engineering blog, support, getting-started guide, changelog, and 19 more developer resources.'
plans:
- name: Schema Org Plans Pricing
  plan_count: 0
  slug: schema-org-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Schema Org Rate Limits
  slug: schema-org-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Schema.org API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: schema-org-jsonschema-spectral-rules
- effective_rule_count: 10
  extends: []
  name: Schema.org API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: schema-org-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 43.2
    contract_quality: 14.7
    developer_ergonomics: 45.2
    discoverability: 74.1
    governance: 43.2
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 31.7
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/schema-org/refs/heads/main/screenshots/schema-org-2026-06-20T193515.png
security:
- kind: domain-security
  name: Schema Org Domain Security
  slug: schema-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: schema-org
tags:
- Schema.org
- Structured Data
- Linked Data
- JSON-LD
- Vocabulary
- SEO
- Web Standards
- RDF
- Ontology
website: https://schema.org/
---

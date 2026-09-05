---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fakerapi Agentic Access
  operation_count: 10
  slug: fakerapi-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- baseURL: https://fakerapi.it/api/v1
  baseurl_source: declared
  description: Generate fake postal addresses with geo coordinates.
  name: FakerAPI Addresses API
  slug: fakerapi-addresses-api
- baseURL: https://fakerapi.it/api/v1
  baseurl_source: declared
  description: Generate fake book records.
  name: FakerAPI Books API
  slug: fakerapi-books-api
- baseURL: https://fakerapi.it/api/v1
  baseurl_source: declared
  description: Generate fake business records.
  name: FakerAPI Companies API
  slug: fakerapi-companies-api
- baseURL: https://fakerapi.it/api/v1
  baseurl_source: declared
  description: Generate fake records with a caller-defined field schema.
  name: FakerAPI Custom API
  slug: fakerapi-custom-api
- baseURL: https://fakerapi.it/api/v1
  baseurl_source: declared
  description: Generate fake image references (titles, descriptions, URLs).
  name: FakerAPI Images API
  slug: fakerapi-images-api
- baseURL: https://fakerapi.it/api/v1
  baseurl_source: declared
  description: Generate fake person profiles with nested addresses.
  name: FakerAPI Persons API
  slug: fakerapi-persons-api
- baseURL: https://fakerapi.it/api/v1
  baseurl_source: declared
  description: Generate fake geographic coordinates.
  name: FakerAPI Places API
  slug: fakerapi-places-api
- baseURL: https://fakerapi.it/api/v1
  baseurl_source: declared
  description: Generate fake product records with images.
  name: FakerAPI Products API
  slug: fakerapi-products-api
- baseURL: https://fakerapi.it/api/v1
  baseurl_source: declared
  description: Generate fake titled text blocks.
  name: FakerAPI Texts API
  slug: fakerapi-texts-api
- baseURL: https://fakerapi.it/api/v1
  baseurl_source: declared
  description: Generate fake application user accounts.
  name: FakerAPI Users API
  slug: fakerapi-users-api
artifact_total: 76
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Faker Addresses API
  slug: open-fakerapi-addresses-api
- collection_type: open
  name: Faker Addresses Books API
  slug: open-fakerapi-books-api
- collection_type: open
  name: Faker Addresses Companies API
  slug: open-fakerapi-companies-api
- collection_type: open
  name: Faker Addresses Custom API
  slug: open-fakerapi-custom-api
- collection_type: open
  name: Faker Addresses Images API
  slug: open-fakerapi-images-api
- collection_type: open
  name: Faker Addresses Persons API
  slug: open-fakerapi-persons-api
- collection_type: open
  name: Faker Addresses Places API
  slug: open-fakerapi-places-api
- collection_type: open
  name: Faker Addresses Products API
  slug: open-fakerapi-products-api
- collection_type: open
  name: Faker Addresses Texts API
  slug: open-fakerapi-texts-api
- collection_type: open
  name: Faker Addresses Users API
  slug: open-fakerapi-users-api
- collection_type: open
  name: FakerAPI
  slug: open-fakerapi
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/pietrantonio91/faker-api/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fakerapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fakerapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fakerapi.it/en
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/pietrantonio91/faker-api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fakerapi-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/fakerapi-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/fakerapi-vocabulary.yml
created: '2026-05-28'
description: FakerAPI is a free, no-authentication REST API that returns realistic fake data for developers, designers, and QA engineers. Built on top of the PHP Faker library by Alessandro Pietrantonio, it exposes a uniform set of GET endpoints for addresses, books, companies, images, persons, places, products, texts, users, and a fully custom resource builder. Every endpoint accepts the same three control parameters (_quantity, _locale, _seed) and returns the same envelope, making it trivial to use for prototypes, mock servers, workshop fixtures, and integration tests.
examples:
- key_count: 6
  name: Fakerapi List Addresses Example
  slug: fakerapi-list-addresses-example
- key_count: 6
  name: Fakerapi List Books Example
  slug: fakerapi-list-books-example
- key_count: 6
  name: Fakerapi List Companies Example
  slug: fakerapi-list-companies-example
- key_count: 6
  name: Fakerapi List Custom Example
  slug: fakerapi-list-custom-example
- key_count: 6
  name: Fakerapi List Images Example
  slug: fakerapi-list-images-example
- key_count: 6
  name: Fakerapi List Persons Example
  slug: fakerapi-list-persons-example
- key_count: 6
  name: Fakerapi List Places Example
  slug: fakerapi-list-places-example
- key_count: 6
  name: Fakerapi List Products Example
  slug: fakerapi-list-products-example
- key_count: 6
  name: Fakerapi List Texts Example
  slug: fakerapi-list-texts-example
- key_count: 6
  name: Fakerapi List Users Example
  slug: fakerapi-list-users-example
features:
- description: Addresses, books, companies, images, persons, places, products, texts, users, and a custom resource builder.
  name: Ten Resource Collections
- description: Every endpoint is open; no API key or registration required.
  name: No Authentication
- description: Generate data in en_US, fr_FR, it_IT, ja_JP, and 60+ other locales via the _locale parameter.
  name: 60+ Locales
- description: Pass _seed to make payloads exactly reproducible across runs.
  name: Deterministic Seeding
- description: Tune _quantity from 1 to 1000 records per request, default 10.
  name: Up to 1000 Records Per Call
- description: /api/v1/custom accepts a caller-defined field map (e.g. name=name, email=email, phone=phoneNumber) and returns matching records.
  name: Custom Schema Endpoint
- description: Every endpoint returns the same {status, code, locale, seed, total, data} shape.
  name: Standard Response Envelope
- description: Service is described as Free, Forever with no published rate limits.
  name: Free Forever
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fakerapi.png
integrations:
- description: FakerAPI is a thin HTTP wrapper over the venerable PHP Faker library by François Zaninotto.
  name: PHP Faker
- description: Trivially imported as a GET-only collection.
  name: Postman / Insomnia
- description: FakerAPI payloads work well as fixture sources for HTTP mocking tools.
  name: Microcks / Prism / MSW
- description: React, Vue, Svelte, Angular, and SolidJS all fetch FakerAPI JSON directly during development.
  name: Frontend Frameworks
json_schemas:
- name: Address
  property_count: 10
  slug: fakerapi-address
- name: Book
  property_count: 9
  slug: fakerapi-book
- name: Company
  property_count: 9
  slug: fakerapi-company
- name: Response Envelope
  property_count: 6
  slug: fakerapi-envelope
- name: Image
  property_count: 3
  slug: fakerapi-image
- name: Person
  property_count: 10
  slug: fakerapi-person
- name: Place
  property_count: 2
  slug: fakerapi-place
- name: Product
  property_count: 11
  slug: fakerapi-product
- name: Text
  property_count: 4
  slug: fakerapi-text
- name: User
  property_count: 11
  slug: fakerapi-user
json_structures:
- name: Fakerapi Address Structure
  property_count: 10
  slug: fakerapi-address-structure
- name: Fakerapi Book Structure
  property_count: 9
  slug: fakerapi-book-structure
- name: Fakerapi Company Structure
  property_count: 9
  slug: fakerapi-company-structure
- name: Fakerapi Envelope Structure
  property_count: 6
  slug: fakerapi-envelope-structure
- name: Fakerapi Image Structure
  property_count: 3
  slug: fakerapi-image-structure
- name: Fakerapi Person Structure
  property_count: 10
  slug: fakerapi-person-structure
- name: Fakerapi Place Structure
  property_count: 2
  slug: fakerapi-place-structure
- name: Fakerapi Product Structure
  property_count: 11
  slug: fakerapi-product-structure
- name: Fakerapi Text Structure
  property_count: 4
  slug: fakerapi-text-structure
- name: Fakerapi User Structure
  property_count: 11
  slug: fakerapi-user-structure
jsonld:
- class_count: 57
  name: Fakerapi Context
  property_count: 1
  slug: fakerapi-context
layout: provider
modified: '2026-05-30'
name: FakerAPI
nav: Providers
network: true
overview: 'FakerAPI publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Books API, Companies API, and 7 more. Tagged areas include Test Data, Fake Data, Mocking, Developer Tools, and Open-Source.


  The FakerAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
random_paper: 16
rules:
- effective_rule_count: 5
  extends: []
  name: FakerAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fakerapi-jsonschema-spectral-rules
- effective_rule_count: 76
  extends:
  - spectral:oas
  name: FakerAPI API Rules
  rule_count: 35
  severity_counts:
    error: 19
    hint: 0
    info: 2
    warn: 14
  slug: fakerapi-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.5
    catalog_earned_first_party: 0.0
    catalog_gap: 35.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 27.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fakerapi/refs/heads/main/screenshots/fakerapi-2026-06-20T181022.png
security:
- kind: domain-security
  name: Fakerapi Domain Security
  slug: fakerapi-domain-security
  summary_line: DNSSEC
slug: fakerapi
tags:
- Test Data
- Fake Data
- Mocking
- Developer Tools
- Open-Source
- Public APIs
use_cases:
- description: Populate React, Vue, or Svelte mockups with realistic data without standing up a backend.
  name: Frontend Prototyping
- description: Use FakerAPI directly or as a fixture source for Microcks, Prism, MSW, or Postman.
  name: API Mocking
- description: Generate deterministic test fixtures (via _seed) for automated browser and API tests.
  name: QA Test Data
- description: Hand learners a single URL to fetch sample data instead of provisioning per-student accounts.
  name: Workshop and Training Fixtures
- description: Seed development databases with thousands of fake users, companies, or products.
  name: Database Seeding
- description: Exercise i18n code paths with names, addresses, and phone numbers in 60+ locales.
  name: Internationalization Testing
- description: Pull large, reproducible JSON payloads to feed load generators.
  name: Load Test Payload Generation
website: https://fakerapi.it/en
---

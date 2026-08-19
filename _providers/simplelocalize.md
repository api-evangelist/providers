---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Simplelocalize Agentic Access
  operation_count: 16
  slug: simplelocalize-agentic-access
  summary_line: 16 operations · 10 acting
api_count: 10
apis:
- description: The SimpleLocalize Language API provides endpoints to create, list, update, and delete languages within a project. Each language is identified by a unique key and requires API key authentication via t
  name: SimpleLocalize Language API
  slug: language-api
- description: The SimpleLocalize Projects API allows creation and listing of translation projects. It uses Personal Token authentication (Bearer) rather than API keys, enabling multi-project management workflows.
  name: SimpleLocalize Projects API
  slug: projects-api
- description: The SimpleLocalize Customer API enables creation and management of customer-specific translations. Customers represent end-user segments with their own translation overrides, identified by a unique cu
  name: SimpleLocalize Customer API
  slug: customer-api
- description: Manage customer-specific translation segments
  name: SimpleLocalize Customers API
  slug: simplelocalize-customers-api
- description: Export translation files in various formats
  name: SimpleLocalize Export API
  slug: simplelocalize-export-api
- description: Import translation files in various formats
  name: SimpleLocalize Import API
  slug: simplelocalize-import-api
- description: Manage project languages
  name: SimpleLocalize Languages API
  slug: simplelocalize-languages-api
- description: Manage translation projects
  name: SimpleLocalize Projects API
  slug: simplelocalize-projects-api
- description: Publish translations to CDN environments
  name: SimpleLocalize Publication API
  slug: simplelocalize-publication-api
- description: Manage translation strings across languages and namespaces
  name: SimpleLocalize Translations API
  slug: simplelocalize-translations-api
artifact_total: 42
collections:
- collection_type: postman
  name: SimpleLocalize Customers API
  slug: postman-simplelocalize-customers-api
- collection_type: postman
  name: SimpleLocalize Customers Export API
  slug: postman-simplelocalize-export-api
- collection_type: postman
  name: SimpleLocalize Customers Import API
  slug: postman-simplelocalize-import-api
- collection_type: postman
  name: SimpleLocalize Customers Languages API
  slug: postman-simplelocalize-languages-api
- collection_type: postman
  name: SimpleLocalize Customers Projects API
  slug: postman-simplelocalize-projects-api
- collection_type: postman
  name: SimpleLocalize Customers Publication API
  slug: postman-simplelocalize-publication-api
- collection_type: postman
  name: SimpleLocalize Customers Translations API
  slug: postman-simplelocalize-translations-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SimpleLocalize Customers API
  slug: open-simplelocalize-customers-api
- collection_type: open
  name: SimpleLocalize Customers Export API
  slug: open-simplelocalize-export-api
- collection_type: open
  name: SimpleLocalize Customers Import API
  slug: open-simplelocalize-import-api
- collection_type: open
  name: SimpleLocalize Customers Languages API
  slug: open-simplelocalize-languages-api
- collection_type: open
  name: SimpleLocalize Customers Projects API
  slug: open-simplelocalize-projects-api
- collection_type: open
  name: SimpleLocalize Customers Publication API
  slug: open-simplelocalize-publication-api
- collection_type: open
  name: SimpleLocalize Customers Translations API
  slug: open-simplelocalize-translations-api
- collection_type: open
  name: SimpleLocalize API
  slug: open-simplelocalize
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/simplelocalize/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simplelocalize-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/simplelocalize-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simplelocalize-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simplelocalize-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simplelocalize
- group: company
  title: ''
  type: Website
  url: https://simplelocalize.io/
- group: docs
  title: ''
  type: Documentation
  url: https://simplelocalize.io/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://simplelocalize.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://simplelocalize.io/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/simplelocalize
- group: build
  title: ''
  type: CLI
  url: https://github.com/simplelocalize/simplelocalize-cli
- group: build
  title: ''
  type: GithubAction
  url: https://github.com/simplelocalize/github-action-cli
- group: build
  title: ''
  type: VSCodeExtension
  url: https://github.com/simplelocalize/vscode-simplelocalize
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/simplelocalize/simplelocalize-mcp-server
- group: build
  title: ''
  type: SDKs
  url: https://github.com/simplelocalize/simplelocalize-cli-npm
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simplelocalize.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simplelocalize.io/privacy-policy/
created: '2025-02-08'
description: SimpleLocalize is a web-based translation management platform that helps small and growing teams save time on handling localization files and translation strings. It provides a REST API for managing translations, languages, projects, and customers, along with integrations for CI/CD pipelines, frameworks, and AI-powered tools.
examples:
- key_count: 4
  name: Simplelocalize Create Translation Example
  slug: simplelocalize-create-translation-example
- key_count: 4
  name: Simplelocalize List Translations Example
  slug: simplelocalize-list-translations-example
finops:
- name: Simplelocalize Finops
  service_category: Localization / Translation Management
  slug: simplelocalize-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simplelocalize.png
json_schemas:
- name: SimpleLocalize Language
  property_count: 2
  slug: simplelocalize-language
- name: SimpleLocalize Project
  property_count: 6
  slug: simplelocalize-project
- name: SimpleLocalize Translation
  property_count: 7
  slug: simplelocalize-translation
json_structures:
- name: Simplelocalize Translation Structure
  property_count: 0
  slug: simplelocalize-translation-structure
jsonld:
- class_count: 17
  name: Simplelocalize Context
  property_count: 3
  slug: simplelocalize-context
layout: provider
modified: '2026-05-19'
name: SimpleLocalize
nav: Providers
network: true
overview: 'SimpleLocalize publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Export API, Import API, and 4 more. Tagged areas include Localization, Translation, and Internationalization.


  The SimpleLocalize catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SimpleLocalize''s developer surface includes authentication, documentation, pricing, engineering blog, CLI, and 13 more developer resources.'
plans:
- name: Simplelocalize Plans Pricing
  plan_count: 5
  slug: simplelocalize-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Simplelocalize Rate Limits
  slug: simplelocalize-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SimpleLocalize API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: simplelocalize-jsonschema-spectral-rules
- effective_rule_count: 8
  extends: []
  name: SimpleLocalize API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: simplelocalize-rules
score:
  band: developing
  composite: 42.5
  delta: -7.2
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 68.7
    developer_ergonomics: 42.9
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/simplelocalize/refs/heads/main/screenshots/simplelocalize-2026-06-20T193932.png
security:
- kind: authentication
  name: Simplelocalize Authentication
  slug: simplelocalize-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Simplelocalize Domain Security
  slug: simplelocalize-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Simplelocalize Vulnerability Disclosure
  slug: simplelocalize-vulnerability-disclosure
  summary_line: disclosure policy published
slug: simplelocalize
tags:
- Localization
- Translation
- Internationalization
website: https://simplelocalize.io/
---

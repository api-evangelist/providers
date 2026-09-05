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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: APIGovernance.Dev provides automated API governance reviews using AI trained on 10,000 public APIs. It offers the API Governance Top-10 best practices list, CI/CD integration, and enterprise governanc
  name: APIGovernance.Dev
  slug: apigovernance-dev
artifact_total: 32
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apigovernance-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apigovernance.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://apigovernance.dev/
- group: commercial
  title: ''
  type: Plans
  url: plans/apigovernance-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apigovernance-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/apigovernance-dev-finops.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apigovernance-dev-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apigovernance-dev-llms.txt
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apigovernance-vocabulary.yaml
- group: design
  title: ''
  type: SpectralRules
  url: rules/apigovernance-dev-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/apigovernance-context.jsonld
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PerfAI-Inc
coverage:
  checked: '2026-09-04'
  detail: 'APIGovernance.Dev sells an AI API-governance review product as an end-user SaaS and publishes no developer surface at all: every discovery path on apigovernance.dev (/openapi.json, /swagger.json, /api-docs, /docs, /llms.txt, /robots.txt and the whole /.well-known/* set) returns a real HTTP 404, there is no docs subdomain, and the one application host the site links to, app.apigovernance.dev, does not complete a TCP connection on port 443 — while the parent company''s own perfai.ai/llms.txt declares the API-governance positioning "outdated" in favour of a different product on a different domain.'
  evidence:
  - status: 200
    url: https://apigovernance.dev/
  - status: 404
    url: https://apigovernance.dev/openapi.json
  - status: 404
    url: https://apigovernance.dev/docs
  - status: 404
    url: https://apigovernance.dev/.well-known/agent-card.json
  - status: 404
    url: https://apigovernance.dev/pricing
  - status: 0
    url: https://app.apigovernance.dev/home
  - status: 200
    url: https://perfai.ai/llms.txt
  reason: no-developer-program
  state: none
created: '2025-01-08'
description: APIGovernance.Dev is an AI-powered API governance platform that enforces API best practices through automated reviews trained on 10,000 public APIs. It provides the API Governance Top-10 list of best practices, automated CI/CD integration, and tools to help organizations deliver consistent, industry-standard APIs. Powered by PerfAI, Inc.
examples:
- key_count: 6
  name: Apigovernance Guideline Example
  slug: apigovernance-guideline-example
- key_count: 5
  name: Apigovernance Policy Example
  slug: apigovernance-policy-example
- key_count: 6
  name: Apigovernance Review Example
  slug: apigovernance-review-example
features:
- description: Automated API governance reviews trained on patterns from 10,000 public APIs.
  name: AI-Powered API Reviews
- description: Curated list of the top 10 API governance best practices across security, design, and documentation.
  name: API Governance Top-10
- description: GitHub Actions and CI/CD pipeline integration for automated governance checks.
  name: CI/CD Integration
- description: Integration with popular API gateways for runtime governance enforcement.
  name: API Gateway Integration
- description: Jira and GitHub Issues integration for governance violation tracking.
  name: Issue Tracking Integration
finops:
- name: Apigovernance Dev Finops
  service_category: API
  slug: apigovernance-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apigovernance-dev.png
integrations:
- description: CI/CD integration for automated governance checks on API specification changes.
  name: GitHub Actions
- description: Create Jira issues for governance violations found during reviews.
  name: Jira
- description: Create GitHub issues for governance violations.
  name: GitHub Issues
- description: Integration with API gateway platforms for runtime policy enforcement.
  name: API Gateways
json_schemas:
- name: Guideline
  property_count: 6
  slug: apigovernance-guideline
- name: Policy
  property_count: 5
  slug: apigovernance-policy
- name: Review
  property_count: 6
  slug: apigovernance-review
json_structures:
- name: Apigovernance Guideline Structure
  property_count: 6
  slug: apigovernance-guideline-structure
- name: Apigovernance Policy Structure
  property_count: 5
  slug: apigovernance-policy-structure
- name: Apigovernance Review Structure
  property_count: 6
  slug: apigovernance-review-structure
jsonld:
- class_count: 5
  name: Apigovernance Context
  property_count: 7
  slug: apigovernance-context
layout: provider
modified: '2026-09-04'
name: APIGovernance.Dev
nav: Providers
network: true
overview: 'APIGovernance.Dev publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, API Governance, Best Practices, Compliance, and Guidelines.


  The APIGovernance.Dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIGovernance.Dev''s developer surface includes pricing and 11 more developer resources.'
plans:
- name: Apigovernance Dev Plans Pricing
  plan_count: 3
  slug: apigovernance-dev-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Apigovernance Dev Rate Limits
  slug: apigovernance-dev-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: APIGovernance.Dev API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apigovernance-dev-jsonschema-spectral-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 73.3
    catalog_earned_first_party: 12.0
    catalog_gap: 41.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 24.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 5.3
  previous_composite: 21.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/apigovernance-dev/refs/heads/main/screenshots/apigovernance-dev-2026-06-20T172239.png
security:
- kind: domain-security
  name: Apigovernance Dev Domain Security
  slug: apigovernance-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apigovernance-dev
solutions:
- description: Basic API governance reviews with the API Governance Top-10 checks.
  name: Free Plan
- description: $199/month with advanced governance automation and CI/CD integration.
  name: Growth Plan
- description: Custom pricing with full governance suite, SSO, and dedicated support.
  name: Enterprise Plan
tags:
- API Design
- API Governance
- Best Practices
- Compliance
- Guidelines
- Standards
use_cases:
- description: Automatically review API specifications against governance guidelines before release.
  name: Automated API Review
- description: Enforce consistent API standards across multiple development teams.
  name: Team Standards Enforcement
- description: Provide developers with actionable best practice guidance during API design.
  name: API Design Guidance
- description: Audit existing APIs for compliance with organizational governance policies.
  name: Compliance Auditing
website: https://apigovernance.dev/
---

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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Openssf Agentic Access
  operation_count: 6
  slug: openssf-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 2
apis:
- description: Sigstore is an OpenSSF-hosted standard and service for signing, verifying, and protecting software. The public-good Sigstore instance exposes Fulcio (code-signing certificate authority) and Rekor (tra
  name: Sigstore Public Good APIs
  slug: sigstore-api
- description: GUAC aggregates software supply-chain security metadata (SBOMs, attestations, vulnerabilities, signatures) into a queryable graph. GUAC exposes a GraphQL API for supply-chain queries when self-hosted.
  name: GUAC (Graph for Understanding Artifact Composition)
  slug: guac-api
- baseURL: https://api.osv.dev
  baseurl_source: declared
  description: The Projects API from OpenSSF — 1 operation(s) for projects.
  name: OpenSSF Projects API
  slug: openssf-projects-api
- baseURL: https://api.osv.dev
  baseurl_source: declared
  description: The Query API from OpenSSF — 1 operation(s) for query.
  name: OpenSSF Query API
  slug: openssf-query-api
- baseURL: https://api.osv.dev
  baseurl_source: declared
  description: The Querybatch API from OpenSSF — 1 operation(s) for querybatch.
  name: OpenSSF Querybatch API
  slug: openssf-querybatch-api
- baseURL: https://api.osv.dev
  baseurl_source: declared
  description: The V1experimental API from OpenSSF — 2 operation(s) for v1experimental.
  name: OpenSSF V1experimental API
  slug: openssf-v1experimental-api
- baseURL: https://api.osv.dev
  baseurl_source: declared
  description: The Vulns API from OpenSSF — 1 operation(s) for vulns.
  name: OpenSSF Vulns API
  slug: openssf-vulns-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OSV (Open Source Vulnerabilities) API
  slug: open-openssf-osv
- collection_type: open
  name: OSV (Open Source Vulnerabilities) Projects API
  slug: open-openssf-projects-api
- collection_type: open
  name: OSV (Open Source Vulnerabilities) Projects Query API
  slug: open-openssf-query-api
- collection_type: open
  name: OSV (Open Source Vulnerabilities) Projects Querybatch API
  slug: open-openssf-querybatch-api
- collection_type: open
  name: OpenSSF Scorecard API
  slug: open-openssf-scorecard
- collection_type: open
  name: OSV (Open Source Vulnerabilities) Projects V1experimental API
  slug: open-openssf-v1experimental-api
- collection_type: open
  name: OSV (Open Source Vulnerabilities) Projects Vulns API
  slug: open-openssf-vulns-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/guacsec/guac/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/guacsec/guac/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/guacsec/guac/blob/main/SECURITY-INSIGHTS.yml
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/guacsec/guac/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/guacsec/guac/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openssf-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openssf-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openssf
- group: company
  title: ''
  type: Website
  url: https://openssf.org/
- group: docs
  title: ''
  type: Documentation
  url: https://openssf.org/resources/
- group: start
  title: ''
  type: Portal
  url: https://openssf.org/projects/
- group: company
  title: ''
  type: Blog
  url: https://openssf.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ossf
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ossf/osv-schema
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ossf/scorecard
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sigstore
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: operate
  title: ''
  type: Community
  url: https://openssf.org/community/
- group: operate
  title: ''
  type: Slack
  url: https://slack.openssf.org/
created: '2026-03-16'
description: The Open Source Security Foundation (OpenSSF) is a collaborative initiative under the Linux Foundation dedicated to improving the security of open source software. It brings together industry leaders, developers, and security experts to address vulnerabilities, enhance supply chain security, and develop security tools and best practices. OpenSSF stewards a number of projects with public REST APIs, including the OSV (Open Source Vulnerabilities) database, the Scorecard automated security health-check service, and Sigstore signing infrastructure.
finops:
- name: Openssf Finops
  service_category: API
  slug: openssf-finops
graphqls:
- description: GUAC aggregates software supply-chain security metadata (SBOMs, attestations, vulnerabilities, signatures) into a queryable graph. GUAC exposes a GraphQL API for supply-chain queries when self-hosted.
  name: OpenSSF GraphQL API
  slug: openssf-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openssf.png
json_schemas:
- name: OSV Vulnerability
  property_count: 14
  slug: openssf-osv-vulnerability
jsonld:
- class_count: 7
  name: Openssf Context
  property_count: 0
  slug: openssf-context
layout: provider
modified: '2026-05-19'
name: OpenSSF
nav: Providers
network: true
overview: 'OpenSSF publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Projects API, Query API, Querybatch API, and 2 more. Tagged areas include Linux Foundation, Open-Source, Security, Supply Chain, and Vulnerabilities.


  The OpenSSF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenSSF''s developer surface includes documentation, developer portal, engineering blog, and 16 more developer resources.'
plans:
- name: Openssf Plans Pricing
  plan_count: 3
  slug: openssf-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Openssf Rate Limits
  slug: openssf-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OpenSSF API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openssf-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 63.3
    catalog_earned_first_party: 0.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 60.3
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openssf/refs/heads/main/screenshots/openssf-2026-06-20T191036.png
security:
- kind: domain-security
  name: Openssf Domain Security
  slug: openssf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openssf
tags:
- Linux Foundation
- Open-Source
- Security
- Supply Chain
- Vulnerabilities
website: https://openssf.org/
---

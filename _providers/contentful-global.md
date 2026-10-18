---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The DesignSystemImport API from Contentful Global — 5 operation(s) for designsystemimport.
  name: Contentful Global Design System Import API
  slug: contentful-global-designsystemimport-api
- description: The DesignSystemSource API from Contentful Global — 6 operation(s) for designsystemsource.
  name: Contentful Global Design System Source API
  slug: contentful-global-designsystemsource-api
- description: The GitHubInstallationRepositories API from Contentful Global — 1 operation(s) for githubinstallationrepositories.
  name: Contentful Global Git Hub Installation Repositories API
  slug: contentful-global-githubinstallationrepositories-api
- description: The GitHubInstallations API from Contentful Global — 3 operation(s) for githubinstallations.
  name: Contentful Global Git Hub Installations API
  slug: contentful-global-githubinstallations-api
- description: The GitHubInstallationStatus API from Contentful Global — 1 operation(s) for githubinstallationstatus.
  name: Contentful Global Git Hub Installation Status API
  slug: contentful-global-githubinstallationstatus-api
- description: The GitHubRepositoryBranches API from Contentful Global — 1 operation(s) for githubrepositorybranches.
  name: Contentful Global Git Hub Repository Branches API
  slug: contentful-global-githubrepositorybranches-api
artifact_total: 8
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contentful-global/refs/heads/main/rules/contentful-global-rules.yml
  title: ''
  type: Spectral
  url: rules/contentful-global-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contentful-global/refs/heads/main/errors/contentful-global-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/contentful-global-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contentful-global/refs/heads/main/conformance/contentful-global-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contentful-global-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contentful-global/refs/heads/main/overlays/contentful-global-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/contentful-global-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contentful-global/refs/heads/main/well-known/contentful-global-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contentful-global-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contentful-global/refs/heads/main/hosts/contentful-global-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contentful-global-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contentful-global/refs/heads/main/vendors/contentful-global-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contentful-global-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contentful-global/refs/heads/main/packages/contentful-global-packages.yml
  title: ''
  type: SDKs
  url: packages/contentful-global-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contentful-global/refs/heads/main/packages/contentful-global-packages.yml
  title: ''
  type: Packages
  url: packages/contentful-global-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.contentful.com/
- group: start
  title: ''
  type: Login
  url: https://be.contentful.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contentful
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contentful-global/refs/heads/main/security/contentful-global-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contentful-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.contentful.com/
coverage:
  checked: '2026-10-10'
  detail: The API host https://api.contentful.com/openapi.json requires an access token and returns no OpenAPI spec.
  evidence:
  - status: 401
    url: https://api.contentful.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Contentful Global is a global headquarter of Contentful, a leading content management platform now part of Salesforce. It provides APIs for managing content, assets, and digital experiences across web, mobile, and other channels. The company offers robust developer tools, extensive documentation, and enterprise-grade features for scaling digital experiences.
image: https://images-www.contentful.com/jtqsy5pye0zd/7lBI01K3NAF1S9JZvC4rkV/478c66f4f3db3ef6c500039d3672049d/image.png
layout: provider
modified: '2026-10-10'
name: Contentful Global
nav: Providers
network: true
overview: 'Contentful Global publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Design System Import API, Design System Source API, Git Hub Installation Repositories API, and 3 more. Tagged areas include Content Management, Software-as-a-Service, Cloud, and Salesforce.


  The Contentful Global catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Contentful Global API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: contentful-global-rules
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 26.5
    catalog_earned_first_party: 0.0
    catalog_gap: 88.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 34.9
    developer_ergonomics: 7.1
    discoverability: 39.3
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: domain-security
  name: Contentful Global Domain Security
  slug: contentful-global-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contentful-global
tags:
- Content Management
- Software-as-a-Service
- Cloud
- Salesforce
website: https://www.contentful.com/
---

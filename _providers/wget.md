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
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'GNU Wget is a free command-line utility for non-interactive downloading of files from the web using HTTP, HTTPS, FTP, and FTPS. It supports recursive downloading, resume of aborted downloads, website '
  name: Wget
  slug: wget
- description: GNU Wget2 is the next-generation successor to GNU Wget, built from scratch around libwget. It is multi-threaded, supports HTTP/2, HTTP compression, parallel connections, If-Modified-Since headers, plu
  name: Wget2
  slug: wget2
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wget-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gnu.org/software/wget/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gnu.org/software/wget/manual/
- group: build
  title: ''
  type: Source Code
  url: https://git.savannah.gnu.org/cgit/wget.git
- group: build
  title: ''
  type: GitHubOrganization
  url: https://gitlab.com/gnuwget
- group: other
  title: ''
  type: Mailing List
  url: https://lists.gnu.org/mailman/listinfo/bug-wget
- group: other
  title: ''
  type: Bug Tracker
  url: https://savannah.gnu.org/bugs/?group=wget
- group: other
  title: ''
  type: Download
  url: https://ftp.gnu.org/gnu/wget/
- group: commercial
  title: ''
  type: License
  url: https://www.gnu.org/licenses/gpl-3.0.html
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/wget/refs/heads/main/vocabulary/wget-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/wget/refs/heads/main/json-ld/wget-context.jsonld
created: '2026-03-27'
description: GNU Wget is a free, open-source command-line utility for non-interactive downloading of files from the web using HTTP, HTTPS, FTP, and FTPS protocols. It supports recursive downloading, resuming aborted downloads, mirroring websites, proxy support, and can be run from scripts and cron jobs. Wget2 is the next-generation successor, written from scratch with multi-threading, HTTP/2, and a plugin API via libwget.
finops:
- name: Wget Finops
  service_category: API
  slug: wget-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wget.png
json_schemas:
- name: Wget Download Request
  property_count: 25
  slug: wget-download-request
- name: Wget2 Plugin
  property_count: 4
  slug: wget2-plugin
json_structures:
- name: Wget Download Request Structure
  property_count: 0
  slug: wget-download-request-structure
- name: Wget2 Plugin Structure
  property_count: 0
  slug: wget2-plugin-structure
jsonld:
- class_count: 48
  name: Wget Context
  property_count: 0
  slug: wget-context
layout: provider
modified: '2026-05-03'
name: Wget
nav: Providers
network: true
overview: 'Wget publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CLI, Clients, HTTP Client, File Download, and Open-Source.


  The Wget catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wget''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Wget Plans Pricing
  plan_count: 3
  slug: wget-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Wget Rate Limits
  slug: wget-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Wget API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wget-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 72.3
    catalog_earned_first_party: 0.0
    catalog_gap: 42.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 24.0
    developer_ergonomics: 15.5
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 18.4
  previous_composite: 24.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wget/refs/heads/main/screenshots/wget-2026-06-20T201415.png
security:
- kind: domain-security
  name: Wget Domain Security
  slug: wget-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wget
tags:
- CLI
- Clients
- HTTP Client
- File Download
- Open-Source
- GNU
website: https://www.gnu.org/software/wget/
---

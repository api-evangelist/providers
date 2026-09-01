---
access_model:
  confidence: high
  label: Free · No credentialing
  onboarding: unknown
  pricing: free
  public: true
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
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tsinghua Agentic Access
  operation_count: 4
  slug: tsinghua-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: 'The TUNA open-source software mirror is the one surface Tsinghua publishes that behaves like a public API. It is operated by TUNA (Tsinghua University TUNA Association), a student association, on the '
  name: Tsinghua University TUNA Open Source Mirror
  slug: tsinghua-mirror-status-api
- description: Tsinghua operates its own Shibboleth Identity Provider and publishes machine-readable SAML 2.0 metadata about it at a public, unauthenticated URL on its own domain. The document declares entityID http
  name: Tsinghua University Identity Provider — SAML 2.0 Federation Metadata
  slug: identity-federation
- description: 'Tsinghua University holds a DataCite membership in its own name — symbol TSINGHUA, memberType direct_member, organizationType academicInstitution, joined 2016-09-05, registered against the university '
  name: Tsinghua University DataCite DOI Registration and Resolution
  slug: datacite-doi
- description: Tsinghua runs its own GitLab instance at git.tsinghua.edu.cn, on its own registrable domain and behind its own identity service — the sign-in page's only form posts to /users/auth/thuid. GitLab expose
  name: Tsinghua University GitLab
  slug: gitlab
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TUNA Mirror Sync Status Mirror Status API
  slug: open-tsinghua-mirror-status-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/tuna/tunasync/blob/master/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tsinghua-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.tsinghua.edu.cn/en/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.tsinghua.edu.cn/en/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.tsinghua.edu.cn/idp/shibboleth
- group: learn
  title: ''
  type: CourseCatalog
  url: https://zhjwxk.cic.tsinghua.edu.cn/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.tsinghua.edu.cn/info/1182/122980.htm
- group: other
  title: ''
  type: AIPolicy
  url: https://www.tsinghua.edu.cn/info/1182/122783.htm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tuna
- group: build
  title: ''
  type: GitHub
  url: https://github.com/THUDM
- group: build
  title: ''
  type: GitHub
  url: https://github.com/thunlp
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tuna/tunasync
- group: docs
  title: ''
  type: Documentation
  url: https://mirrors.tuna.tsinghua.edu.cn/help/AOSP/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tsinghua-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/tsinghua-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tsinghua-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/tsinghua-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tsinghua-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tsinghua-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tsinghua-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tsinghua-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tsinghua-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tsinghua-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tsinghua University (清华大学) is a public national research university in Beijing, China, a member of the C9 League and the Double First-Class construction programme, and one of the highest-ranked universities in Asia. Its programmable footprint is small, real, and almost entirely invisible from outside the campus network. Tsinghua operates no developer portal, no open data portal and no API key issuance of any kind: api.tsinghua.edu.cn, open.tsinghua.edu.cn and data.tsinghua.edu.cn do not resolve. Every system the university runs for its own community — the learning platform (learn.tsinghua.edu.cn), course registration (zhjwxk.cic.tsinghua.edu.cn), the institutional GitLab (git.tsinghua.edu.cn), Tsinghua Cloud (cloud.tsinghua.edu.cn), the information portal and the campus card — terminates at one electronic identity service, id.tsinghua.edu.cn, and is unreachable without institutional affiliation. What Tsinghua does publish, unauthenticated and machine-readable, is three things,
  and all three are the institution''s own rather than a vendor''s. First, the TUNA open-source mirror (mirrors.tuna.tsinghua.edu.cn), run by the student TUNA association on the university''s own domain and infrastructure, which serves two live JSON documents: the tunasync synchronization status of every mirrored repository, and a catalog of the installable images for 66 distributions, font collections and applications. Second, and more consequential for a university, Tsinghua runs its own Shibboleth Identity Provider at idp.tsinghua.edu.cn and publishes SAML 2.0 federation metadata about it — entityID https://idp.tsinghua.edu.cn/idp/shibboleth, shibmd:Scope tsinghua.edu.cn — with every SingleSignOnService and SingleLogoutService location resolving to a Tsinghua host rather than to a federation vendor. Third, the university library holds a DataCite direct membership in its own name (symbol TSINGHUA, joined 2016) under which 194 DOIs are registered on prefix 10.23650, resolving to datacite.lib.tsinghua.edu.cn.
  Two honest qualifications belong in this description. The DOI landing-page host completes TCP and TLS but returns nothing to an HTTP GET after 60 seconds from outside China, so those 194 DOIs are registered but unresolvable from here. And the mirror''s edge answers HTTP 403 to requests carrying a desktop-browser User-Agent while answering the same request 200 for a plain tool User-Agent — the inverse of the usual bot filter, and enough to lock out any agent that spoofs a browser. Notably, Tsinghua holds no Figshare, Elsevier Pure, Symplectic, Ex Libris or Dataverse tenancy that could be found: unlike most of this cohort, there is no vendor contract masquerading as this institution''s engineering. Tsinghua research groups (THUDM, THUNLP, THUML, TUNA) publish substantial open-source code on GitHub, but those are project repositories, not an institutional API programme, and they are recorded as pointers rather than as surfaces.'
examples:
- key_count: 2
  name: Tsinghua Getmirrorisocatalog Example
  slug: tsinghua-getMirrorIsoCatalog-example
finops:
- name: Tsinghua Finops
  service_category: Education
  slug: tsinghua-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tsinghua.png
json_schemas:
- name: IsoCatalogEntry
  property_count: 3
  slug: tsinghua-mirror-isoinfo
- name: MirrorStatus
  property_count: 13
  slug: tsinghua-mirror-status
json_structures:
- name: Tsinghua Mirror Status Structure
  property_count: 13
  slug: tsinghua-mirror-status-structure
jsonld:
- class_count: 11
  name: Tsinghua Context
  property_count: 6
  slug: tsinghua-context
layout: provider
modified: '2026-08-19'
name: Tsinghua University
nav: Providers
network: true
overview: 'Tsinghua University publishes 2 APIs on the [APIs.io](https://apis.io/) network: TUNA Open Source Mirror and Identity Provider — SAML 2.0 Federation Metadata. Tagged areas include Education, Higher Education, University, China, and Beijing.


  The Tsinghua University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tsinghua University''s developer surface includes GitHub presence, documentation, authentication, and 21 more developer resources.'
plans:
- name: Tsinghua Plans Pricing
  plan_count: 2
  slug: tsinghua-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Tsinghua Rate Limits
  slug: tsinghua-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tsinghua University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tsinghua-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Tsinghua University API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: tsinghua-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 33.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tsinghua/refs/heads/main/screenshots/tsinghua-2026-06-20T195921.png
security:
- kind: authentication
  name: Tsinghua Authentication
  slug: tsinghua-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tsinghua Domain Security
  slug: tsinghua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tsinghua
tags:
- Education
- Higher Education
- University
- China
- Beijing
- C9 League
- Research
- Open-Source
- Mirror
- Identity Federation
- Shibboleth
- SAML
- Research Data
- DOI
- Library
website: https://www.tsinghua.edu.cn/en/
---

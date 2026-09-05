---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Fatcat Agentic Access
  operation_count: 96
  slug: fatcat-agentic-access
  summary_line: 96 operations · 42 acting
api_count: 1
apis:
- baseURL: https://api.fatcat.wiki/v0
  baseurl_source: declared
  description: 'Helper methods and internal APIs for editor authentication. # TAGLINE'
  name: Fatcat auth API
  slug: fatcat-auth-api
- baseURL: https://api.fatcat.wiki/v0
  baseurl_source: declared
  description: 'The **Changelog** is the ordered feed of editgroups which have been # TAGLINE accepted into the catalog. # TAGLINE'
  name: Fatcat changelog API
  slug: fatcat-changelog-api
- baseURL: https://api.fatcat.wiki/v0
  baseurl_source: declared
  description: '**Container** entities represent publication venues like journals, # TAGLINE conference proceedings, book series, or blogs. They group publications # TAGLINE ("releases"). # TAGLINE See the "Catalog S'
  name: Fatcat containers API
  slug: fatcat-containers-api
- baseURL: https://api.fatcat.wiki/v0
  baseurl_source: declared
  description: '**Creator** entities represent individuals (or organizations, or other # TAGLINE agents) who contribute to the creation of specific releases # TAGLINE (publications). # TAGLINE See the "Catalog Style '
  name: Fatcat creators API
  slug: fatcat-creators-api
- baseURL: https://api.fatcat.wiki/v0
  baseurl_source: declared
  description: '**Editgroups** are sets of changes, each to individual entities in the # TAGLINE catalog. Every edit must be part of an editgroup which is reviewed and # TAGLINE accepted (merged) as a whole. # TAGLIN'
  name: Fatcat editgroups API
  slug: fatcat-editgroups-api
- baseURL: https://api.fatcat.wiki/v0
  baseurl_source: declared
  description: '**Editors** are human user accounts and bots that make changes to the # TAGLINE Fatcat catalog. # TAGLINE The API allows fetching (and updating) metadata about individual editors, # TAGLINE as well as'
  name: Fatcat editors API
  slug: fatcat-editors-api
- baseURL: https://api.fatcat.wiki/v0
  baseurl_source: declared
  description: '**File** entities represent unique digital files which are full # TAGLINE manifestations of specific releases (publications), such as fulltext PDF # TAGLINE files, JATS XML documents, or video files. '
  name: Fatcat files API
  slug: fatcat-files-api
- baseURL: https://api.fatcat.wiki/v0
  baseurl_source: declared
  description: '**Fileset** entities represent sets of digital files, as well as locations # TAGLINE where they can be found on the public web. Filesets most commonly # TAGLINE represent datasets consisting of severa'
  name: Fatcat filesets API
  slug: fatcat-filesets-api
- baseURL: https://api.fatcat.wiki/v0
  baseurl_source: declared
  description: '**Release** entities represent specific published versions of a research # TAGLINE work, such as a pre-print, a journal article, a book (or chapter), or a # TAGLINE scholarly blog post. Releases are a'
  name: Fatcat releases API
  slug: fatcat-releases-api
- baseURL: https://api.fatcat.wiki/v0
  baseurl_source: declared
  description: '**Web Capture** entities represent archival snapshots of web pages (or # TAGLINE other web resources), which are usually complete manifestations of a # TAGLINE specific release entity. Web Captures al'
  name: Fatcat webcaptures API
  slug: fatcat-webcaptures-api
- baseURL: https://api.fatcat.wiki/v0
  baseurl_source: declared
  description: '**Work** entities group several Release entities which are different # TAGLINE versions of the same abstract piece of research. For example, three # TAGLINE release entities representing the pre-print'
  name: Fatcat works API
  slug: fatcat-works-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: fatcat auth API
  slug: open-fatcat-auth-api
- collection_type: open
  name: fatcat auth changelog API
  slug: open-fatcat-changelog-api
- collection_type: open
  name: fatcat auth containers API
  slug: open-fatcat-containers-api
- collection_type: open
  name: fatcat auth creators API
  slug: open-fatcat-creators-api
- collection_type: open
  name: fatcat auth editgroups API
  slug: open-fatcat-editgroups-api
- collection_type: open
  name: fatcat auth editors API
  slug: open-fatcat-editors-api
- collection_type: open
  name: fatcat auth files API
  slug: open-fatcat-files-api
- collection_type: open
  name: fatcat auth filesets API
  slug: open-fatcat-filesets-api
- collection_type: open
  name: fatcat auth releases API
  slug: open-fatcat-releases-api
- collection_type: open
  name: fatcat auth webcaptures API
  slug: open-fatcat-webcaptures-api
- collection_type: open
  name: fatcat auth works API
  slug: open-fatcat-works-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fatcat-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/internetarchive/fatcat/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/internetarchive/fatcat/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fatcat-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fatcat-authentication.yml
created: '2026-06-13'
description: Fatcat is a versioned, user-editable open catalog of published research works maintained by the Internet Archive. It tracks bibliographic metadata, links papers to full-text copies, and preserves access to scholarly publications including journal articles, conference proceedings, and datasets across millions of research works.
examples:
- key_count: 12
  name: Container Entity Example
  slug: container-entity-example
- key_count: 9
  name: Creator Entity Example
  slug: creator-entity-example
- key_count: 7
  name: Editgroup Example
  slug: editgroup-example
- key_count: 11
  name: File Entity Example
  slug: file-entity-example
- key_count: 21
  name: Release Entity Example
  slug: release-entity-example
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://fatcat.wiki/static/fatcat_logo.svg
json_schemas:
- name: ContainerEntity
  property_count: 13
  slug: container-entity
- name: CreatorEntity
  property_count: 10
  slug: creator-entity
- name: Editgroup
  property_count: 8
  slug: editgroup
- name: FileEntity
  property_count: 13
  slug: file-entity
- name: ReleaseEntity
  property_count: 26
  slug: release-entity
jsonld:
- class_count: 8
  name: context Context
  property_count: 65
  slug: context
layout: provider
modified: '2026-06-13'
name: Fatcat
nav: Providers
network: true
overview: 'Fatcat publishes 11 APIs on the [APIs.io](https://apis.io/) network, including auth API, changelog API, containers API, and 8 more. Tagged areas include Scholarly, Research, Academic, Open Access, and Bibliographic.


  The Fatcat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fatcat''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 18
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Fatcat API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: fatcat-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 62.3
    catalog_earned_first_party: 0.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 57.1
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Fatcat Authentication
  slug: fatcat-authentication
  summary_line: apiKey · 1 scheme
slug: fatcat
tags:
- Scholarly
- Research
- Academic
- Open Access
- Bibliographic
- Publications
- Metadata
- Internet Archive
website: https://fatcat.wiki/
---

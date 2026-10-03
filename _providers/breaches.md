---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 31
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering data breach intelligence, credential exposure databases, dark-web monitoring, and leak detection APIs. Breach intelligence platforms aggregate compromised credentials, stealer logs, ransomware leak-site posts, underground forum chatter, and dark-web marketplace listings into queryable APIs that security teams use to detect exposure of their organization, employees, customers, executives, and supply-chain partners. This collection indexes services like Have I Been Pwned for consumer breach lookup, Pwned Passwords for k-anonymity credential checks, enterprise breach intelligence platforms (CrowdStrike, Microsoft Defender, SentinelOne, Splunk), credential and identity exposure monitors (Okta, Auth0, 1Password, LastPass, Bitwarden), vulnerability and exposure feeds (NVD, CISA, Qualys, Rapid7, Tanium), and regulatory breach-notification authorities (CISA, FTC, NIST) that publish machine-readable feeds of disclosed breaches and known-exploited
  vulnerabilities.
examples:
- key_count: 16
  name: Breaches Breach Record Example
  slug: breaches-breach-record-example
- key_count: 11
  name: Breaches Exposed Credential Example
  slug: breaches-exposed-credential-example
features:
- description: APIs like Have I Been Pwned let consumers and security teams check whether an email address, username, or phone number has appeared in known data breaches and stealer log corpora.
  name: Email and Account Breach Lookup
- description: The Pwned Passwords API exposes 800+ million breached password hashes through a k-anonymity protocol, letting applications block known-compromised credentials without transmitting full hashes.
  name: Pwned Password Checking (K-Anonymity)
- description: Enterprise breach intelligence platforms continuously scrape dark-web marketplaces, ransomware leak sites, Telegram channels, and underground forums for mentions of customer data, executives, brands, and credentials.
  name: Dark Web and Underground Forum Monitoring
- description: Modern breach intelligence increasingly centers on infostealer malware logs (RedLine, Raccoon, Vidar, LummaC2) that capture browser-stored credentials, session cookies, and crypto wallets at scale.
  name: Stealer Log and Credential Exposure Feeds
- description: Threat intelligence APIs track ransomware group leak sites (LockBit, Cl0p, ALPHV, Akira) to surface newly disclosed victim organizations and stolen data postings as they appear.
  name: Ransomware Leak-Site Tracking
- description: Authoritative vulnerability databases (NVD, CISA KEV) and commercial exposure platforms (Qualys, Rapid7, Tanium) expose CVE, CVSS, and known-exploited-vulnerability metadata via API.
  name: Vulnerability and Exposure Feeds
- description: Government authorities (FTC, state AGs, EU DPAs, HHS) publish disclosed breach filings; security teams ingest these feeds to track third-party and supply-chain breach exposure.
  name: Regulatory Breach Notification Feeds
- description: Identity providers (Okta, Auth0) and password managers (1Password, Bitwarden, LastPass) integrate with breach feeds to block re-use of known-compromised passwords and force resets on exposed accounts.
  name: Credential Stuffing Defense
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: The canonical consumer breach-lookup service with 13+ billion breached accounts and 800+ million pwned passwords accessible via free and paid API tiers.
  name: Have I Been Pwned
- description: Enterprise threat intelligence platform with adversary tracking, dark-web monitoring, and breach exposure feeds delivered via the Falcon API.
  name: CrowdStrike Falcon Intelligence
- description: Threat intelligence and breach exposure feeds integrated across Microsoft Defender, Sentinel, and Graph Security APIs.
  name: Microsoft Defender Threat Intelligence
- description: SIEM platform that ingests breach intelligence and credential exposure feeds for correlation against authentication and access logs.
  name: Splunk Enterprise Security
- description: Authoritative catalog of CVEs with evidence of active exploitation, published by the US Cybersecurity and Infrastructure Security Agency as a machine-readable feed.
  name: CISA Known Exploited Vulnerabilities (KEV)
- description: The National Vulnerability Database REST API exposing CVE records, CVSS scores, CPE mappings, and CWE classifications used as the foundation of breach root-cause analysis.
  name: NVD CVE API
- description: Identity platforms that integrate breach-password feeds to block known-compromised credentials and trigger step-up authentication on suspected account takeover.
  name: Okta and Auth0
- description: Consumer and enterprise password manager that surfaces breach exposure for stored credentials via integration with Have I Been Pwned and proprietary feeds.
  name: 1Password Watchtower
json_schemas:
- name: BreachRecord
  property_count: 16
  slug: breaches-breach-record
- name: ExposedCredential
  property_count: 12
  slug: breaches-exposed-credential
json_structures:
- name: Breaches Breach Record Structure
  property_count: 16
  slug: breaches-breach-record-structure
- name: Breaches Exposed Credential Structure
  property_count: 12
  slug: breaches-exposed-credential-structure
jsonld:
- class_count: 8
  name: Breaches Context
  property_count: 27
  slug: breaches-context
layout: provider
modified: '2026-05-19'
name: Breaches
nav: Providers
network: true
overview: 'Breaches is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data Breach, Credential Exposure, Dark Web Monitoring, Threat Intelligence, and Leak Detection.


  The Breaches catalog on APIs.io includes 1 JSON-LD context.


  Breaches'' developer surface includes developer portal and 1 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: breaches
tags:
- Data Breach
- Credential Exposure
- Dark Web Monitoring
- Threat Intelligence
- Leak Detection
- Breach Notification
- Stealer Logs
- Pwned Passwords
use_cases:
- description: Security teams continuously query breach intelligence APIs for corporate email domains to detect employee credentials exposed in third-party breaches and infostealer logs, triggering forced password resets.
  name: Employee Credential Exposure Monitoring
- description: Consumer applications integrate Pwned Passwords and breach lookup APIs at signup and login to block known-compromised credentials and notify customers of exposure.
  name: Customer Account Takeover Prevention
- description: Brand and executive protection teams use dark-web monitoring APIs to detect doxxing, leaked personal data, and impersonation targeting C-suite, board members, and high-value employees.
  name: Executive and VIP Protection
- description: GRC teams ingest breach-notification feeds and regulatory disclosures via API to track breach incidents at vendors, suppliers, and partners that handle their data.
  name: Third-Party and Supply-Chain Risk
- description: Threat intel teams subscribe to ransomware leak-site feeds via API to alert on newly named victims relevant to their industry, supply chain, or geography.
  name: Ransomware Victim Intelligence
- description: Vulnerability management teams combine NVD CVE data, CISA's Known Exploited Vulnerabilities (KEV) catalog, and commercial exposure platforms to prioritize patching based on breach exploitation evidence.
  name: Vulnerability Prioritization
- description: Privacy and legal teams query FTC, state AG, and EU DPA breach-notification APIs to track required disclosures and benchmark their own incident response.
  name: Regulatory Breach Disclosure Compliance
- description: AI agents wired to breach intelligence APIs autonomously enrich security alerts with exposure context, correlate stolen credentials with active sessions, and draft incident-response runbooks.
  name: AI Agent Breach Triage
website: https://apievangelist.com
---

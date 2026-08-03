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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: The U.S. Cyber Command Cyber National Mission Force (CNMF) shares unclassified malware samples on VirusTotal via the CYBERCOM_Malware_Alert account. This public threat intelligence sharing program pos
  name: CNMF Malware Sharing via VirusTotal
  slug: cnmf-virustotal-malware-sharing
- description: Public news releases, advisories, and operational announcements from U.S. Cyber Command. Includes joint cybersecurity advisories, malware disclosure announcements, defensive cyber operations public st
  name: USCYBERCOM News and Advisories
  slug: uscybercom-news-media
artifact_total: 31
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-cyber-command-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USCYBERCOM
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/united-states-cyber-command
- group: company
  title: ''
  type: Website
  url: https://www.cybercom.mil/
- group: docs
  title: News and Advisories
  type: Documentation
  url: https://www.cybercom.mil/Media/News/
- group: operate
  title: Contact USCYBERCOM
  type: Contact
  url: https://www.cybercom.mil/About/Contact/
- group: design
  title: US Cyber Command Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/us-cyber-command/refs/heads/main/vocabulary/us-cyber-command-vocabulary.yml
- group: design
  title: US Cyber Command JSON-LD Context
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/us-cyber-command/refs/heads/main/json-ld/us-cyber-command-context.jsonld
created: '2024-12-25'
description: US Cyber Command (USCYBERCOM) is a Unified Combatant Command of the United States Armed Forces responsible for directing, synchronizing, and coordinating cyberspace operations. It defends Department of Defense information networks and prepares to conduct full spectrum military cyberspace operations to ensure freedom of action in cyberspace and deny the same to adversaries. USCYBERCOM's Cyber National Mission Force (CNMF) publicly shares unclassified malware samples attributed to state-sponsored threat actors via VirusTotal, contributing to the global cybersecurity community's threat intelligence capabilities. USCYBERCOM also collaborates with CISA, NSA, and allied nations on joint cybersecurity advisories and threat disclosures.
examples:
- key_count: 12
  name: Uscybercom Advisory Example
  slug: uscybercom-advisory-example
- key_count: 13
  name: Uscybercom Malware Sample Example
  slug: uscybercom-malware-sample-example
- key_count: 11
  name: Uscybercom Threat Actor Example
  slug: uscybercom-threat-actor-example
features:
- description: The Cyber National Mission Force (CNMF) shares unclassified malware samples on VirusTotal (CYBERCOM_Malware_Alert) attributed to state-sponsored threat actors from Russia, Iran, North Korea, and other adversaries.
  name: CNMF Malware Sharing Program
- description: USCYBERCOM publishes joint cybersecurity advisories with CISA, NSA, FBI, and allied nation cybersecurity agencies on active threats and recommended mitigations.
  name: Joint Cybersecurity Advisories
- description: USCYBERCOM conducts defensive cyber operations to detect and respond to malicious cyber activity targeting U.S. and partner networks, sharing findings through public disclosures.
  name: Defensive Cyber Operations
- description: Published guidance identifying high-priority cybersecurity challenge problems for industry, academia, and government collaboration to advance national cyber defense capabilities.
  name: Cyber Command Challenge Problems
- description: At partner nation invitation, USCYBERCOM deploys hunt forward teams to identify malicious cyber activity on allied networks, with findings sometimes shared publicly via VirusTotal.
  name: Hunt Forward Operations
finops:
- name: Us Cyber Command Finops
  service_category: API
  slug: us-cyber-command-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-cyber-command.png
integrations:
- description: CNMF publishes malware samples to VirusTotal via the CYBERCOM_Malware_Alert account for public analysis and sharing.
  name: VirusTotal
- description: USCYBERCOM collaborates with CISA on joint cybersecurity advisories, malware disclosures, and critical infrastructure defense.
  name: CISA (Cybersecurity and Infrastructure Security Agency)
- description: USCYBERCOM and NSA coordinate on threat intelligence sharing and jointly author cybersecurity advisories on nation-state threats.
  name: NSA Cybersecurity Directorate
- description: USCYBERCOM partners with UK NCSC, Canadian CCCS, Australian ACSC, and New Zealand NCSC for joint threat intelligence and advisory publications.
  name: Five Eyes Alliance
json_schemas:
- name: CybersecurityAdvisory
  property_count: 12
  slug: uscybercom-advisory
- name: MalwareSample
  property_count: 13
  slug: uscybercom-malware-sample
- name: ThreatActor
  property_count: 11
  slug: uscybercom-threat-actor
json_structures:
- name: Uscybercom Advisory Structure
  property_count: 12
  slug: uscybercom-advisory-structure
- name: Uscybercom Malware Sample Structure
  property_count: 13
  slug: uscybercom-malware-sample-structure
- name: Uscybercom Threat Actor Structure
  property_count: 11
  slug: uscybercom-threat-actor-structure
jsonld:
- class_count: 6
  name: Us Cyber Command Context
  property_count: 29
  slug: us-cyber-command-context
layout: provider
modified: '2026-05-03'
name: US Cyber Command
nav: Providers
network: true
overview: 'US Cyber Command publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Federal Government, Military, Threat Intelligence, and Defense.


  The US Cyber Command catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  US Cyber Command''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Us Cyber Command Plans Pricing
  plan_count: 3
  slug: us-cyber-command-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Us Cyber Command Rate Limits
  slug: us-cyber-command-rate-limits
rules:
- name: US Cyber Command API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: us-cyber-command-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 33.9
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 37.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-cyber-command/refs/heads/main/screenshots/us-cyber-command-2026-06-20T200614.png
security:
- kind: domain-security
  name: Us Cyber Command Domain Security
  slug: us-cyber-command-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: us-cyber-command
tags:
- Cybersecurity
- Federal Government
- Military
- Threat Intelligence
- Defense
use_cases:
- description: Security analysts and threat hunters use CNMF VirusTotal uploads to identify and analyze state-sponsored malware, updating detection rules and IOC databases.
  name: Threat Intelligence Enrichment
- description: Security researchers analyze USCYBERCOM-disclosed malware samples to understand adversary TTPs, develop detection signatures, and support attribution analysis.
  name: Malware Analysis and Attribution
- description: Organizations and security teams track USCYBERCOM joint advisories to understand active threats and implement recommended mitigations.
  name: Cybersecurity Advisory Tracking
- description: Security tool developers use CNMF malware samples to test and improve detection capabilities, antivirus signatures, and threat hunting tools.
  name: Defensive Tool Development
- description: Government agencies and critical infrastructure operators monitor USCYBERCOM disclosures for nation-state threat indicators relevant to their networks.
  name: Government Threat Awareness
website: https://www.cybercom.mil/
---

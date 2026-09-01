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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: The original Simple Network Management Protocol defined in RFC 1157 (May 1990). Establishes the five core PDUs (GetRequest, GetNextRequest, GetResponse, SetRequest, Trap), community-string authenticat
  name: SNMPv1 (RFC 1157)
  slug: snmpv1
- description: Community-based SNMPv2, the most widely deployed version of SNMP in production today. Adds the GetBulkRequest PDU for efficient table retrieval and the InformRequest PDU for acknowledged notifications
  name: SNMPv2c (RFC 1901-1908)
  slug: snmpv2c
- description: The modular SNMPv3 management framework. RFC 3411 defines the SNMP engine, Message Processing Subsystem, Security Subsystem, and Access Control Subsystem; RFC 3414 specifies the User-based Security Mo
  name: SNMPv3 Architecture (RFC 3411-3418)
  slug: snmpv3
- description: The canonical SNMP MIB module for network interface management, published June 2000. Defines ifTable, ifXTable, ifStackTable, and ifRcvAddressTable, plus the ifType enumeration registered by IANA. Uni
  name: IF-MIB (RFC 2863) — The Interfaces Group MIB
  slug: if-mib
- description: Structure of Management Information — the data definition language and naming scheme that every MIB module is written against. The IANA SMI Numbers registry administers the OID hierarchy rooted at 1.3
  name: SMI and the OID Tree
  slug: smi
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/net-snmp/net-snmp/issues
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snmp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datatracker.ietf.org/wg/opsawg/about/
- group: docs
  title: ''
  type: Specification
  url: https://datatracker.ietf.org/doc/html/rfc3411
- group: docs
  title: ''
  type: Documentation
  url: https://www.net-snmp.org/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/net-snmp/net-snmp
- group: start
  title: ''
  type: Registry
  url: https://www.iana.org/assignments/smi-numbers/smi-numbers.xhtml
created: '2025-01-01'
description: Simple Network Management Protocol (SNMP) is the foundational IETF standard for monitoring and managing network devices. SNMP defines a request/response protocol over UDP (ports 161 and 162) for retrieving and altering management variables exposed by agents on routers, switches, servers, UPSs, and other equipment, plus an asynchronous trap/notification channel for event delivery. The protocol family spans three major generations — SNMPv1 (RFC 1157), SNMPv2c (RFC 1901-1908), and the modular SNMPv3 architecture (RFC 3411-3418, extended by RFC 7860 for HMAC-SHA-2 authentication) — and is paired with the Structure of Management Information (SMI) and a vast catalog of MIB modules, most notably the IF-MIB (RFC 2863) for network interfaces. SNMP remains the lingua franca of network monitoring, consumed primarily by NMS platforms such as Nagios, Zabbix, PRTG, SolarWinds, LibreNMS, and Observium, and implemented in open source primarily by the Net-SNMP suite.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snmp.png
jsonld:
- class_count: 31
  name: Snmp Context
  property_count: 7
  slug: snmp-context
layout: provider
modified: '2026-05-23'
name: SNMP
nav: Providers
network: true
overview: 'SNMP publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SNMP, Network Management, Network Monitoring, IETF, and Protocol.


  The SNMP catalog on APIs.io includes 1 JSON-LD context.


  SNMP''s developer surface includes documentation and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  open_source:
    applies: true
    score: 0.0
  previous_composite: 10.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snmp/refs/heads/main/screenshots/snmp-2026-06-20T194107.png
security:
- kind: domain-security
  name: Snmp Domain Security
  slug: snmp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: snmp
tags:
- SNMP
- Network Management
- Network Monitoring
- IETF
- Protocol
- MIB
- SMI
- OID
- Agents
- Traps
- UDP
website: https://datatracker.ietf.org/wg/opsawg/about/
---

---
api_count: 3
apis:
- description: REST/JSON administration API for a GroupWise system, served by the GroupWise Administration Service that installs alongside the GroupWise agents. Introduced under the "Windermere" codename for GroupWi
  name: GroupWise Administration REST API
  slug: groupwise-administration-rest-api
- description: Server-side SOAP protocol for reading and writing a GroupWise user's mailbox, spoken directly to the GroupWise Post Office Agent over HTTP/HTTPS. 96 documented methods defined in the methods.xsd schem
  name: GroupWise Web Services (SOAP)
  slug: groupwise-web-services-soap
- description: DSML v2 for eDirectory ships a deployable Java web archive (.war) that exposes Novell eDirectory as a SOAP web service using DSML - the OASIS Directory Services Markup Language standard for representi
  name: DSML for eDirectory (SOAP)
  slug: dsml-for-edirectory-soap
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.novell.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.novell.com/developer/ndk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.novell.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://www.novell.com/documentation/developer/groupwise_sdk/
- group: build
  title: ''
  type: Packages
  url: packages/novell-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/novell-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/novell-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/novell-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/novell-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/novell-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/novell-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/novell-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.microfocus.com/lifecycle/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/novell-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/novell-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/novell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/novell-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novell-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/novell-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://support.novell.com/security-alerts/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.novell.com/developer/ndk/groupwise/develop_to_groupwise.html
created: '2026-09-13'
description: 'Novell, Inc. was a Provo, Utah network-software company best known for NetWare, eDirectory, GroupWise and ZENworks. It was acquired by The Attachmate Group in 2011, folded into Micro Focus with the 2014 Attachmate acquisition, and passed to OpenText when OpenText bought Micro Focus in 2023. The Novell corporate brand is retired and novell.com is now an OpenText-operated redirector, but a large part of the Novell developer surface is still served on www.novell.com and is not merely archival: the Novell Developer Kit (NDK) A-Z index, the eDirectory developer kits (which now 301 to microfocus.com), and the GroupWise SDK documentation set published per release right up to GroupWise 25. Two callable API surfaces are documented there - the GroupWise Administration REST API (220 resource paths, 357 operations, served by the customer''s own GroupWise Administration Service on port 9710) and the GroupWise Web Services SOAP protocol against the Post Office Agent (96 documented methods
  on port 7191). Both are customer-hosted, not SaaS: there is no Novell-operated endpoint, no key to obtain and no sign-up. No machine-readable contract is obtainable - a WSDL is referenced by name but shipped only inside SDK archives on hosts that no longer resolve, and the Admin API''s WADL is generated at runtime on the customer''s own server. The documentation outlived the distribution.'
image: https://www.novell.com/favicon.ico
layout: provider
modified: '2026-09-13'
name: Novell
nav: Providers
network: true
overview: 'Novell publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, enterprise_software, collaboration, email, and directory_services.


  Novell''s developer surface includes documentation, API reference, authentication, changelog, getting-started guide, and 16 more developer resources.'
plans:
- name: Novell Plans Pricing
  plan_count: 0
  slug: novell-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Novell Rate Limits
  slug: novell-rate-limits
security:
- kind: authentication
  name: Novell Authentication
  slug: novell-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Novell Domain Security
  slug: novell-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Novell Vulnerability Disclosure
  slug: novell-vulnerability-disclosure
  summary_line: disclosure policy published
slug: novell
tags:
- Company
- enterprise_software
- collaboration
- email
- directory_services
- identity
- groupware
- ldap
- soap
- legacy
- self_hosted
- endpoint_management
website: https://www.novell.com/
---

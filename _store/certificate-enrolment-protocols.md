---
aid: certificate-enrolment-protocols
url: https://raw.githubusercontent.com/api-evangelist/certificate-enrolment-protocols/refs/heads/main/apis.yml
name: Certificate Enrolment Protocols
tags:
  - ACME
  - Automation
  - CMP
  - Certificates
  - Cryptography
  - EST
  - IETF
  - Let's Encrypt
  - PKI
  - RFC
  - Renewal
  - SCEP
  - Security
  - Standards
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-01'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: Certificate Enrolment Protocols are the interoperable standards that automate the lifecycle operations of requesting, issuing, renewing, and revoking X.509 digital certificates between Certificate Authorities (CAs), Registration Authorities (RAs), and end entities. The four major protocols in active deployment are ACME (RFC 8555, widely adopted via Let's Encrypt and cert-manager for web PKI), SCEP (legacy Simple Certificate Enrollment Protocol widely supported in network devices and MDM), EST (RFC 7030, Enrollment over Secure Transport for modern HTTPS-capable devices), and CMP (RFC 4210 / RFC 9480, Certificate Management Protocol for enterprise PKI and industrial automation). This index tracks the specifications, reference implementations, and supporting infrastructure for each.
apis:
  - aid: certificate-enrolment-protocols:acme-rfc-8555
    name: ACME - Automatic Certificate Management Environment (RFC 8555)
    tags:
      - ACME
      - Let's Encrypt
      - RFC 8555
      - Web PKI
    humanURL: https://datatracker.ietf.org/doc/html/rfc8555
    properties:
      - url: https://datatracker.ietf.org/doc/html/rfc8555
        type: Specification
      - url: https://letsencrypt.org/docs/
        type: ReferenceImplementation
      - url: https://github.com/letsencrypt/boulder
        type: SourceCode
      - url: https://cert-manager.io/docs/configuration/acme/
        type: Integration
    description: ACME is an IETF standard defined in RFC 8555 that automates the interactions between CAs and web servers for validating domain control (http-01, dns-01, tls-alpn-01 challenges), issuing, renewing, and revoking X.509 certificates. ACME is the protocol behind Let's Encrypt, ZeroSSL, and most cloud CAs, and is implemented in clients including certbot, acme.sh, Lego, win-acme, and cert-manager.
  - aid: certificate-enrolment-protocols:scep
    name: SCEP - Simple Certificate Enrollment Protocol
    tags:
      - IoT
      - MDM
      - Network Devices
      - SCEP
    humanURL: https://datatracker.ietf.org/doc/html/rfc8894
    properties:
      - url: https://datatracker.ietf.org/doc/html/rfc8894
        type: Specification
      - url: https://en.wikipedia.org/wiki/Simple_Certificate_Enrollment_Protocol
        type: Overview
      - url: https://github.com/micromdm/scep
        type: SourceCode
    description: SCEP is a PKCS#7 / PKCS#10-based certificate enrollment protocol originally developed by Cisco in the late 1990s and standardized as informational RFC 8894. Despite its age, SCEP remains the dominant enrollment protocol for routers, switches, VPN concentrators, and mobile device management platforms (Apple MDM, Microsoft Intune).
  - aid: certificate-enrolment-protocols:est-rfc-7030
    name: EST - Enrollment over Secure Transport (RFC 7030)
    tags:
      - EST
      - IoT
      - RFC 7030
      - TLS
    humanURL: https://datatracker.ietf.org/doc/html/rfc7030
    properties:
      - url: https://datatracker.ietf.org/doc/html/rfc7030
        type: Specification
      - url: https://datatracker.ietf.org/doc/html/rfc8951
        type: Updates
      - url: https://github.com/cisco/libest
        type: SourceCode
    description: EST provides HTTPS-based certificate enrollment over TLS, using mutual authentication or TLS with certificate-less client authentication to establish a secure channel before PKCS#10 enrollment. EST targets modern HTTPS-capable IoT and network devices that need simpler deployment than CMP but more secure transport than SCEP.
  - aid: certificate-enrolment-protocols:cmp-rfc-4210
    name: CMP - Certificate Management Protocol (RFC 4210 / RFC 9480)
    tags:
      - CMP
      - Enterprise PKI
      - Industrial
      - RFC 4210
      - RFC 9480
    humanURL: https://datatracker.ietf.org/doc/html/rfc4210
    properties:
      - url: https://datatracker.ietf.org/doc/html/rfc4210
        type: Specification
      - url: https://datatracker.ietf.org/doc/html/rfc9480
        type: LightweightCMP
      - url: https://github.com/mpeylo/cmpclient
        type: SourceCode
    description: CMP provides comprehensive certificate lifecycle management including initialization, key update, revocation, cross-certification, and recovery for enterprise and industrial PKI environments. CMP messages carry their own cryptographic protection independent of the transport and are commonly used in 3GPP mobile networks, industrial automation, and telco infrastructure.
  - aid: certificate-enrolment-protocols:cert-manager
    name: cert-manager (Kubernetes ACME Client)
    tags:
      - ACME
      - CNCF
      - Client
      - Kubernetes
    humanURL: https://cert-manager.io/
    properties:
      - url: https://cert-manager.io/
        type: Website
      - url: https://cert-manager.io/docs/configuration/acme/
        type: Documentation
      - url: https://github.com/cert-manager/cert-manager
        type: SourceCode
    description: cert-manager is a CNCF Graduated Kubernetes controller that acts as an ACME, Vault, Venafi, and CA client to automatically issue and renew certificates declaratively for workloads and Ingress/Gateway API objects.
  - aid: certificate-enrolment-protocols:certbot
    name: Certbot (ACME Reference Client)
    tags:
      - ACME
      - Certbot
      - EFF
      - Let's Encrypt
    humanURL: https://certbot.eff.org/
    properties:
      - url: https://certbot.eff.org/
        type: Website
      - url: https://eff-certbot.readthedocs.io/
        type: Documentation
      - url: https://github.com/certbot/certbot
        type: SourceCode
    description: Certbot, maintained by the Electronic Frontier Foundation (EFF), is the reference ACME client used to obtain and renew Let's Encrypt and other ACME CA certificates on web and mail servers with a focus on automation and Apache/Nginx plugin support.
common:
  - type: Website
    url: https://en.wikipedia.org/wiki/Certificate_enrollment
  - type: IETF
    url: https://datatracker.ietf.org/
  - type: LetsEncrypt
    url: https://letsencrypt.org/
  - type: CertManager
    url: https://cert-manager.io/
  - type: Certbot
    url: https://certbot.eff.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

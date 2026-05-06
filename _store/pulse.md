---
aid: pulse
name: Pulse
description: APIs for Ivanti Pulse Secure (formerly Pulse Secure), providing secure remote access VPN, network access control, and zero trust access solutions.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/pulse/refs/heads/main/apis.yml
tags:
  - Ivanti
  - Network Security
  - Secure Access
  - SSL VPN
  - VPN
  - Zero Trust
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - aid: pulse:ivanti-connect-secure-rest-api
    name: Ivanti Connect Secure REST API
    description: REST API for managing Ivanti Connect Secure (formerly Pulse Connect Secure) VPN appliances. Provides endpoints for system configuration, user and role management, authentication server configuration, license management, network settings, resource policies, and system maintenance operations.
    humanURL: https://help.ivanti.com/ps/help/en_US/IPS/vNow/pcs-pps-rest-api/landingpage.htm
    tags:
      - Authentication
      - Configuration
      - Network Security
      - Secure Access
      - SSL VPN
      - VPN
    properties:
      - type: Documentation
        url: https://help.ivanti.com/ps/help/en_US/IPS/vNow/pcs-pps-rest-api/landingpage.htm
  - aid: pulse:ivanti-policy-secure-rest-api
    name: Ivanti Policy Secure REST API
    description: REST API for managing Ivanti Policy Secure (formerly Pulse Policy Secure) network access control appliances.
    humanURL: https://help.ivanti.com/ps/help/en_US/IPS/vNow/pcs-pps-rest-api/landingpage.htm
    tags:
      - NAC
      - Network Access Control
      - Policy
      - Security
    properties:
      - type: Documentation
        url: https://help.ivanti.com/ps/help/en_US/IPS/vNow/pcs-pps-rest-api/landingpage.htm
  - aid: pulse:ivanti-neurons-zero-trust-rest-api
    name: Ivanti Neurons for Zero Trust Access REST API
    description: REST API for managing Ivanti Neurons for Zero Trust Access (nZTA), providing endpoints for managing zero trust access policies, gateways, and user access.
    humanURL: https://help.ivanti.com/ps/help/en_US/nSA/22.x/nsa-zta/api/landingpage.htm
    tags:
      - Secure Access
      - Zero Trust
      - ZTNA
    properties:
      - type: Documentation
        url: https://help.ivanti.com/ps/help/en_US/nSA/22.x/nsa-zta/api/landingpage.htm
common:
  - type: Website
    url: https://www.ivanti.com/products/connect-secure-vpn
  - type: Documentation
    url: https://www.ivanti.com/support/product-documentation
  - type: PrivacyPolicy
    url: https://www.ivanti.com/company/legal/privacy-policy
  - type: TermsOfService
    url: https://www.ivanti.com/company/legal
  - type: Status
    url: https://status.ivanticloud.com/
  - type: Blog
    url: https://www.ivanti.com/blog
  - type: Community
    url: https://forums.ivanti.com/s/welcome-pulse-secure?language=en_US
  - type: Features
    data:
      - name: SSL VPN Remote Access
        description: Secure remote access to corporate resources through SSL VPN tunnels with granular access policies.
      - name: Zero Trust Network Access
        description: Identity-aware, application-level access control without exposing network resources.
      - name: Network Access Control
        description: Enforce security policies on endpoints before granting network access with 802.1X and agent-based checks.
      - name: Multi-Factor Authentication
        description: Integrate with MFA providers for strong authentication on VPN and network access.
      - name: Host Checker
        description: Validate endpoint compliance with security policies before granting access.
      - name: Role-Based Access Control
        description: Define granular access policies based on user roles, device type, and compliance status.
  - type: UseCases
    data:
      - name: Remote Workforce Access
        description: Provide secure remote access to corporate applications and resources for distributed teams.
      - name: Zero Trust Architecture
        description: Implement zero trust security with per-application access controls and continuous verification.
      - name: BYOD Management
        description: Securely enable bring-your-own-device access with endpoint compliance checking.
      - name: Partner and Contractor Access
        description: Grant controlled, time-limited access to third-party partners and contractors.
  - type: Integrations
    data:
      - name: Microsoft Active Directory
        description: Authenticate users against Active Directory for single sign-on and role mapping.
      - name: RADIUS Servers
        description: Integrate with RADIUS for centralized authentication and accounting.
      - name: SIEM Platforms
        description: Forward access logs and security events to SIEM platforms for monitoring and analysis.
      - name: MDM Solutions
        description: Integrate with mobile device management solutions for endpoint compliance verification.
      - name: Identity Providers
        description: Connect with SAML and OIDC identity providers for federated authentication.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

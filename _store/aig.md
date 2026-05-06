---
aid: aig
url: https://raw.githubusercontent.com/api-evangelist/aig/refs/heads/main/apis.yml
name: AIG
tags:
  - Insurance
  - Financial Services
  - Property Casualty
  - Cyber Insurance
  - Enterprise
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-17'
modified: '2026-04-19'
position: Consumer
description: American International Group, Inc. (AIG) is a global insurance organization founded in 1919 and operating in over 200 countries and jurisdictions. AIG provides comprehensive risk solutions including property casualty, cyber, professional liability, casualty, specialty insurance, and reinsurance services for individuals and businesses. AIG operates digital portals for brokers and clients including myAIG for North America brokers and IntelliRisk Advanced for claims management, but does not currently offer a public developer API.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
apis:
  - aid: aig:aig
    name: AIG Insurance
    tags:
      - Insurance
      - Property Casualty
      - Cyber
      - Professional Liability
      - Specialty
    humanURL: https://www.aig.com
    description: AIG offers commercial and personal insurance products globally including property casualty, cyber insurance, casualty, professional liability, financial lines, specialty risk, and reinsurance. AIG serves multinational corporations, financial institutions, governments, and individuals.
    properties:
      - url: https://www.aig.com
        type: Website
      - url: https://www.aig.com/business
        type: Documentation
        title: Business Insurance
      - url: https://www.aig.com/individual
        type: Documentation
        title: Individual Insurance
      - url: https://myaig.aig.com
        type: Portal
        title: myAIG Broker Portal
      - url: https://www.aig.com/home/resources/global-network/claims
        type: Portal
        title: Claims Portal
common:
  - name: AIG Website
    url: https://www.aig.com
    type: Website
    description: AIG main website with company information and insurance products.
  - name: AIG Business Insurance
    url: https://www.aig.com/business
    type: Documentation
    description: Commercial insurance products and risk solutions for businesses.
  - name: AIG Individual Insurance
    url: https://www.aig.com/individual
    type: Documentation
    description: Personal insurance products including travel, accident, and private client.
  - name: myAIG Broker Portal
    url: https://myaig.aig.com
    type: Portal
    description: Online portal for North America brokers to access AIG services.
  - name: AIG IntelliRisk
    url: https://www.aig.com/business/insurance/workers-compensation/intellirisk
    type: Portal
    description: IntelliRisk Advanced claims management platform.
  - name: AIG Privacy Policy
    url: https://www.aig.com/about-us/privacy
    type: PrivacyPolicy
    description: AIG privacy policy and data practices.
  - name: AIG Terms of Use
    url: https://www.aig.com/about-us/terms-and-conditions
    type: TermsOfService
    description: Terms and conditions for AIG services.
  - name: AIG Investor Relations
    url: https://www.aig.com/about-us/investors
    type: Portal
    description: Investor relations including financial reports and SEC filings.
  - name: AIG Careers
    url: https://jobs.aig.com
    type: Portal
    description: AIG careers and job opportunities portal.
  - type: Features
    data:
      - name: Global Commercial Insurance
        description: Property casualty, financial lines, specialty, and other commercial insurance in 200+ countries.
      - name: Cyber Insurance
        description: Cyber risk solutions protecting organizations from data breaches, ransomware, and cyber liability.
      - name: Professional Liability
        description: Directors and Officers (D&O), Errors and Omissions (E&O), and employment practices liability.
      - name: Multinational Insurance Programs
        description: Coordinated global insurance programs for multinational corporations with local and global coverage.
      - name: Claims Management
        description: Global claims expertise with IntelliRisk Advanced platform for self-administered claims programs.
      - name: myAIG Digital Portal
        description: Broker portal providing online access to policy information, endorsements, and certificates.
      - name: Private Client Group
        description: High-value personal insurance for homes, autos, collections, and liability for wealthy individuals.
      - name: Travel Insurance
        description: Travel protection plans for trip cancellation, medical emergencies, and travel-related risks.
  - type: UseCases
    data:
      - name: Enterprise Risk Management
        description: Comprehensive risk transfer solutions for large corporations across property, liability, and specialty lines.
      - name: Cyber Risk Transfer
        description: Protect businesses from financial losses due to cyber incidents, data breaches, and regulatory fines.
      - name: Multinational Program Administration
        description: Coordinate insurance coverage for global operations with consistent terms across jurisdictions.
      - name: Financial Institution Risk
        description: Bankers blanket bond, fidelity, professional liability, and other coverages for financial institutions.
      - name: Construction and Infrastructure
        description: Contractor liability, builders risk, and environmental coverages for construction projects.
  - type: Integrations
    data:
      - name: Broker Management Systems
        description: Integration with broker platforms for quoting, binding, and policy management via myAIG portal.
      - name: Risk Management Information Systems
        description: Data feeds and integrations with RMIS platforms for risk data management.
      - name: Anthropic AI
        description: Partnership with Anthropic to implement AI for insurance operations and underwriting enhancement.
      - name: ERP Integration
        description: Enterprise resource planning integration for certificate management and compliance tracking.
---

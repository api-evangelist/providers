---
aid: chewy
name: Chewy
x-type: company
description: Chewy, Inc. is a Fortune 500 American online retailer of pet food, pet products, prescription medications, and veterinary services headquartered in Plantation, Florida. Chewy is one of the largest e-commerce pet retailers in the United States and supports a customer-focused operating model centered on subscription Autoship orders, Chewy Pharmacy prescription fulfillment, Connect with a Vet telehealth, and Chewy Health insurance. Chewy provides vendor and supplier integration primarily through the Dsco supplier integration platform rather than a public consumer-facing developer API. The Dsco-based integration supports core EDI transactions for purchase orders, inventory updates, shipment confirmations, and invoices, enabling brands and third-party logistics providers to connect with Chewy's e-commerce marketplace.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/chewy/refs/heads/main/apis.yml
tags:
  - Autoship
  - Drop Shipping
  - Dsco
  - E-Commerce
  - EDI
  - Fortune 500
  - Pet Food
  - Pet Pharmacy
  - Pet Retail
  - Plantation
  - Subscriptions
  - Telehealth
  - Vendor Integration
  - Veterinary
created: '2026-03-21'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: chewy:vendor-integration-api
    name: Chewy Vendor Integration API
    description: Chewy provides vendor and supplier integration through the Dsco platform, enabling third-party brands and logistics providers to connect with Chewy's e-commerce marketplace. The integration supports EDI transactions including purchase orders (850), inventory updates (846), shipment confirmations (856), and invoices (810). Vendors authenticate using API tokens and supplier account credentials provided through the Dsco platform.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.chewy.com
    baseURL: https://api.dsco.io
    tags:
      - Dsco
      - E-Commerce
      - EDI
      - Pet Retail
      - Vendor Integration
    properties:
      - type: Documentation
        url: https://www.chewy.com
      - type: PartnerProgram
        url: https://www.chewy.com/about
      - type: DscoPlatform
        url: https://www.dsco.io
common:
  - type: Website
    url: https://www.chewy.com
  - type: GitHub
    url: https://github.com/Chewy-Inc
  - type: InvestorRelations
    url: https://investor.chewy.com
  - type: Newsroom
    url: https://newsroom.chewy.com
  - type: Careers
    url: https://careers.chewy.com
  - type: HelpCenter
    url: https://www.chewy.com/app/help
  - type: TermsOfUse
    url: https://www.chewy.com/app/content/terms-of-use
  - type: PrivacyPolicy
    url: https://www.chewy.com/app/content/privacy
  - type: ChewyPharmacy
    url: https://www.chewy.com/app/content/chewy-pharmacy
  - type: ConnectWithAVet
    url: https://www.chewy.com/app/content/connect-with-a-vet
  - type: ChewyHealth
    url: https://www.chewyhealth.com
  - name: Brands
    type: Brands
    data:
      - name: Chewy
      - name: Chewy Pharmacy
      - name: Chewy Health
      - name: Connect With a Vet
      - name: American Journey
      - name: Tylee's
      - name: Frisco
      - name: Vibeful
  - name: Features
    type: Features
    data:
      - name: Online Pet Retail
      - name: Autoship Subscriptions
      - name: Chewy Pharmacy
      - name: Connect With a Vet (Telehealth)
      - name: Pet Insurance
      - name: Multi-Pet Households
      - name: Donations and Adoptions
      - name: Same-Day and Next-Day Delivery
      - name: Vendor Drop-Ship Integration via Dsco
      - name: EDI Order, Inventory, Ship, Invoice Cycle
  - name: UseCases
    type: UseCases
    data:
      - name: Pet Food and Treat Subscriptions
      - name: Prescription Pet Medication Fulfillment
      - name: Vet Telehealth Consultations
      - name: Pet Health Insurance
      - name: Pet Brand Drop-Ship Marketplace
      - name: Third-Party Logistics Integration
      - name: Adoption Partner Donations
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

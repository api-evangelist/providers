---
aid: orange
name: Orange
description: Orange Developer offers a portfolio of network, communication, identity, location, payment, IoT, and cloud APIs that allow developers to build new customer experiences powered by programmable networks and Orange's telecom infrastructure across Europe, the Middle East, and Africa.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Network
  - Telecom
  - Identity
  - Messaging
  - Location
  - Payment
  - IoT
created: '2025-02-09'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/orange/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: orange:number-verification
    name: Number Verification API
    description: Verifies phone numbers in real time against the operator network for identity confirmation, fraud prevention, and frictionless authentication.
    humanURL: https://docs.developer.orange.com/network-apis/api-catalog/number-verification/playground/1.0/overview
    tags:
      - Identity
      - Verification
      - Network
    properties:
      - type: Documentation
        url: https://docs.developer.orange.com/network-apis/api-catalog/number-verification/playground/1.0/overview
  - aid: orange:sim-swap
    name: SIM Swap API
    description: Detects recent SIM card changes for a given mobile number to help prevent account takeover and fraud.
    humanURL: https://docs.developer.orange.com/network-apis/api-catalog/sim-swap/playground/1.0/overview
    tags:
      - Fraud Prevention
      - Identity
      - Network
    properties:
      - type: Documentation
        url: https://docs.developer.orange.com/network-apis/api-catalog/sim-swap/playground/1.0/overview
  - aid: orange:kyc-match
    name: KYC Match API
    description: Conducts know-your-customer matching against operator-held subscriber data to validate identities during onboarding.
    humanURL: https://docs.developer.orange.com/network-apis/api-catalog/kyc-match/playground/0.2/overview
    tags:
      - Identity
      - KYC
      - Compliance
    properties:
      - type: Documentation
        url: https://docs.developer.orange.com/network-apis/api-catalog/kyc-match/playground/0.2/overview
  - aid: orange:device-swap
    name: Device Swap API
    description: Identifies recent changes of the device associated with a mobile number to flag potential fraud and verify continuity of identity.
    humanURL: https://docs.developer.orange.com/network-apis/api-catalog/device-swap/es/0.1/overview
    tags:
      - Fraud Prevention
      - Network
    properties:
      - type: Documentation
        url: https://docs.developer.orange.com/network-apis/api-catalog/device-swap/es/0.1/overview
  - aid: orange:live-identity
    name: Live Identity API
    description: Identity verification suite including Live Identity Captcha and Live Identity Verify for confirming a real, present user.
    humanURL: https://developer.orange.com/apis/live-identity-verify
    tags:
      - Identity
      - Verification
    properties:
      - type: Documentation
        url: https://developer.orange.com/apis/live-identity-verify
      - type: Captcha
        url: https://developer.orange.com/apis/live-identity-captcha
  - aid: orange:messaging
    name: Messaging APIs
    description: A portfolio of messaging APIs including SMS Middle East and Africa, Messaging Pro Cameroon, Voice as a Service, Business Talk, and Contact Everyone for enterprise and regional communications.
    humanURL: https://developer.orange.com/apis/
    tags:
      - Messaging
      - SMS
      - Voice
    properties:
      - type: Documentation
        url: https://developer.orange.com/apis/
  - aid: orange:device-location
    name: Device Location APIs
    description: Device Location Retrieval and Device Location Verification APIs that obtain or confirm a device's geographic position from the network.
    humanURL: https://developer.orange.com/apis/
    tags:
      - Location
      - Network
    properties:
      - type: Documentation
        url: https://developer.orange.com/apis/
  - aid: orange:geofencing
    name: Geofencing API
    description: Establishes geographic boundary alerts based on real-time device location served by the operator network.
    humanURL: https://developer.orange.com/apis/
    tags:
      - Location
      - Geofencing
    properties:
      - type: Documentation
        url: https://developer.orange.com/apis/
  - aid: orange:network-dynamics
    name: Network Dynamics APIs
    description: Network insight APIs including Population Density Data, Quality of Service on Demand, Device Reachability Status, and Device Roaming Status.
    humanURL: https://developer.orange.com/apis/
    tags:
      - Network
      - Quality of Service
      - Insights
    properties:
      - type: Documentation
        url: https://developer.orange.com/apis/
  - aid: orange:orange-money
    name: Orange Money API
    description: Mobile payment platform API enabling developers to integrate Orange Money wallet transactions, transfers, and payments.
    humanURL: https://developer.orange.com/apis/
    tags:
      - Payment
      - Wallet
      - Mobile Money
    properties:
      - type: Documentation
        url: https://developer.orange.com/apis/
  - aid: orange:pay-with-orange-bill
    name: Pay with Orange Bill API
    description: Direct carrier billing API allowing customers to charge purchases to their Orange mobile bill.
    humanURL: https://developer.orange.com/apis/
    tags:
      - Payment
      - Carrier Billing
    properties:
      - type: Documentation
        url: https://developer.orange.com/apis/
  - aid: orange:cloud-connectivity
    name: Cloud Connectivity APIs
    description: A set of cloud and connectivity APIs including Cloud Avenue, Evolution Platform, EVPL Online, and Content Delivery Boost.
    humanURL: https://developer.orange.com/apis/
    tags:
      - Cloud
      - Connectivity
    properties:
      - type: Documentation
        url: https://developer.orange.com/apis/
  - aid: orange:iot
    name: IoT Managed Global Connectivity API
    description: SIM management and device monitoring for IoT deployments across Orange's global cellular footprint.
    humanURL: https://developer.orange.com/apis/
    tags:
      - IoT
      - Connectivity
      - SIM
    properties:
      - type: Documentation
        url: https://developer.orange.com/apis/
common:
  - type: Portal
    url: https://developer.orange.com/
  - type: Documentation
    url: https://developer.orange.com/apis/
  - type: Sign Up
    url: https://developer.orange.com/user/register
  - type: Login
    url: https://developer.orange.com/user/login
  - type: Terms of Service
    url: https://developer.orange.com/terms-conditions
  - type: Privacy Policy
    url: https://developer.orange.com/privacy-policy
  - type: Support
    url: https://developer.orange.com/forum
  - type: Website
    url: https://www.orange.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

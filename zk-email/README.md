**ZK-Email**

By April 2024, we released 1) a custom account recovery solution via email guardians for account abstraction wallets, and 2) a login with zk email flow with ECDSA key authorization.

The flow of account recovery will be that AA wallets specify email addresses as guardians, those email addresses receive emails to accept gaurdianship, and if the keys are ever lost and the wallet needs to be recovered, then guardians can simply send an email with the users new public key, to save their assets after a timelock.
The flow of login with email will be that users put in their email addresses into a website, they get a magic link style email in their inbox from a relayer with a hidden link authorizing an ephemeral key, and any reply to that email confirms that ephemeral key as the signer for that email address on any website.  That website can continue to use that browser-specific temporary ECDSA keypair until the user switches devices, at which point they can do the flow again to authorize additional ECDSA keypairs.  This will be a completely decentralized drop-in replacement for signin with email for crypto-native apps that expect ECDSA signers


**Lagrange RUN RUL**
https://lagrangedao.org/spaces/0x129ddcdA5B114c05d4932CC553535Ef3cC9201D5/ZK-Email/app

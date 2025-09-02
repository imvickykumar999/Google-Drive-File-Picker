# *Pick Files from Google Drive*

<img width="1301" height="630" alt="image" src="https://github.com/user-attachments/assets/440db3e6-2bc4-4eec-b436-6c830e6c2810" />

You’ll need to create and configure a project in the **Google Cloud Console** to get both your **Client ID** (for OAuth) and **API Key** (for Drive API/Picker). Here’s a step-by-step:

---

## 1. Create a Google Cloud project

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Sign in with your Google account.
3. At the top left, click the **project dropdown** → **New Project**.
4. Give it a name (e.g., *Drive Picker Demo*) → click **Create**.

---

## 2. Enable required APIs

1. In your project, go to **APIs & Services > Library**.
2. Enable the following:

   * **Google Drive API**
   * **Google Picker API**

---

## 3. Create OAuth 2.0 Client ID (for `GOOGLE_CLIENT_ID`)

1. In the left menu, go to **APIs & Services > Credentials**.
2. Click **Create Credentials** → **OAuth client ID**.
3. You may be asked to configure the **OAuth consent screen**:

   * Choose **External** if not in Google Workspace.
   * Fill in app name, user support email, etc.
   * Add scopes: `https://www.googleapis.com/auth/drive.readonly`.
   * Add your test users (your Google account at least).
   * Save.
4. Back in **Create OAuth client ID**:

   * Choose **Web application**.
   * Give it a name (e.g., *Drive Picker App*).
   * Under **Authorized JavaScript origins**, add your domain (e.g., `http://localhost:5500` while developing).
   * Under **Authorized redirect URIs**, you can leave blank (Picker doesn’t need it).
5. Click **Create** → copy the **Client ID** → this is your `GOOGLE_CLIENT_ID`.

---

## 4. Create an API Key (for `GOOGLE_API_KEY`)

1. Still in **Credentials**, click **Create Credentials** → **API key**.
2. Copy the generated API key → this is your `GOOGLE_API_KEY`.
3. For security, click **Restrict key**:

   * **API restrictions**: limit to *Google Picker API* and *Google Drive API*.
   * **Application restrictions**: restrict by HTTP referrers (e.g., `http://localhost:5500/*` for development, your real domain in production).

---

✅ Now you can plug them into your `.env` file.

---

⚠️ **Important**:

* Use API Key only in client-side apps if you’ve restricted it to your domain.
* Keep OAuth Client ID safe; it’s fine in frontend code but don’t share your Client Secret.

<img width="1322" height="655" alt="image" src="https://github.com/user-attachments/assets/a52d02b7-8229-4b6e-a9ab-a9902e6da8f0" />

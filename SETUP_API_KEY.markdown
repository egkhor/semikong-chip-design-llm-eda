# How to Obtain and Set the Synopsys API Key

This guide explains how to obtain a `SYNOPSYS_API_KEY` for the **SemiKong Chip Design LLM** project and configure it to enable EDA integration with Synopsys tools, as used in `src/eda_integration.py`. The API key authenticates requests to the Synopsys API (placeholder: `https://api.synopsys.com/design-compiler/validate`) for validating design recommendations.

## Step 1: Obtain a Synopsys API Key

The `SYNOPSYS_API_KEY` is provided by Synopsys for accessing their EDA tool APIs (e.g., Design Compiler). Follow these steps:

1. **Check License Access**:
   - Confirm if your organization, academic institution, or Synopsys license includes API access. Contact your IT/admin team or Synopsys account manager.
   - For individuals, explore Synopsys’ academic programs (e.g., [Synopsys University Program](https://www.synopsys.com/community/university-program.html)) or trial licenses, though API access may be limited.

2. **Register for an API Key**:
   - Visit the Synopsys developer portal or support site ([https://www.synopsys.com/support.html](https://www.synopsys.com/support.html)).
   - Sign in with your Synopsys account (SolvNet) or create one.
   - Navigate to the API section (e.g., “Developer Tools” or “API Keys”). If unavailable, contact Synopsys support ([support@synopsys.com](mailto:support@synopsys.com)) or sales ([sales@synopsys.com](mailto:sales@synopsys.com)), mentioning your use case for chip design optimization in this open-source project.
   - Request an API key for Design Compiler or the relevant tool. Copy the key (e.g., `abc123xyz789`).

3. **Alternative for Testing**:
   - If you lack API access, use mock data by modifying `eda_integration.py` to return simulated responses (see [Troubleshooting](#troubleshooting)).
   - Consider open-source EDA tools like OpenROAD for future contributions, as they don’t require proprietary keys.

**Note**: The API URL in `eda_integration.py` is a placeholder. Verify the correct endpoint via Synopsys documentation or support.

## Step 2: Set the API Key

Set the `SYNOPSYS_API_KEY` environment variable to authenticate API requests. Choose one of the following methods:

### Option A: Temporary (Current Terminal Session)

1. Open a terminal (macOS/Linux: Terminal; Windows: Command Prompt).
2. Run, replacing `your_key` with your API key:
   ```bash
   export SYNOPSYS_API_KEY=abc123xyz789  # macOS/Linux
   set SYNOPSYS_API_KEY=abc123xyz789     # Windows
   ```
3. Verify:
   ```bash
   echo $SYNOPSYS_API_KEY  # macOS/Linux
   echo %SYNOPSYS_API_KEY% # Windows
   ```
4. Run the script:
   ```bash
   python src/eda_integration.py
   ```

**Note**: This resets when the terminal closes.

### Option B: Persistent (Across Sessions)

Add the key to your shell profile for macOS/Linux or system environment for Windows.

#### macOS/Linux
1. Determine your shell:
   ```bash
   echo $SHELL
   ```
   - Zsh (macOS default): Edit `~/.zshrc`
   - Bash: Edit `~/.bash_profile` or `~/.bashrc`

2. Open the file:
   ```bash
   nano ~/.zshrc  # or ~/.bash_profile
   ```
3. Add:
   ```bash
   export SYNOPSYS_API_KEY=abc123xyz789
   ```
4. Save (Ctrl+O, Enter, Ctrl+X in nano).
5. Apply:
   ```bash
   source ~/.zshrc  # or ~/.bash_profile
   ```
6. Verify:
   ```bash
   echo $SYNOPSYS_API_KEY
   ```

#### Windows
1. Right-click “This PC” > Properties > Advanced system settings > Environment Variables.
2. Under “User variables”, click “New”.
3. Set:
   - Variable name: `SYNOPSYS_API_KEY`
   - Variable value: `abc123xyz789`
4. Click OK to save.
5. Restart Command Prompt or IDE.
6. Verify:
   ```cmd
   echo %SYNOPSYS_API_KEY%
   ```

### Option C: Use a `.env` File (Recommended)

1. Install `python-dotenv`:
   ```bash
   pip install python-dotenv
   ```
2. Create `.env` in the project root:
   ```bash
   touch .env
   nano .env
   ```
3. Add:
   ```
   SYNOPSYS_API_KEY=abc123xyz789
   ```
4. Save and exit.
5. Ensure `.env` is ignored by Git:
   - Check `.gitignore` includes:
     ```
     .env
     ```
6. Update `eda_integration.py` to load the key:
   ```python
   from dotenv import load_dotenv
   import os
   load_dotenv()
   API_KEY = os.getenv("SYNOPSYS_API_KEY")
   ```
7. Run:
   ```bash
   python src/eda_integration.py
   ```

## Step 3: Test the Setup

1. Run the EDA script:
   ```bash
   python src/eda_integration.py
   ```
2. Check for:
   - Success: `EDA-validated dataset saved to data/text_notes/eda_validated_data.csv`
   - Errors: “EDA API error” (e.g., invalid key or endpoint)

## Troubleshooting

- **Key Not Found**: If `os.getenv("SYNOPSYS_API_KEY")` is `None`, recheck export or `.env` setup.
- **API Error**: Verify the API key and endpoint with Synopsys support. For testing, mock the API in `eda_integration.py`:
  ```python
  def validate_design(note_text, recommendation):
      return {"power": 0.5, "area": 1.0, "timing": 0.05}
  ```
- **Dependencies**: Ensure `requests` and `python-dotenv` are installed (`pip install -r requirements.txt`).
- **Placeholder URL**: If `https://api.synopsys.com/design-compiler/validate` fails, check Synopsys documentation for the correct endpoint.

## Security Best Practices

- **Never Commit Keys**: Do not hardcode `SYNOPSYS_API_KEY` in scripts or commit to GitHub.
- **Use `.env`**: Store keys in `.env` and ensure `.gitignore` includes it.
- **Restrict Access**: Share keys only with authorized team members.

## Contribute

- Share feedback or mock EDA data via [GitHub Issues](https://github.com/egkhor/semikong-chip-design-llm/issues).
- Propose open-source EDA tool integrations (e.g., OpenROAD) in [Discussions](https://github.com/egkhor/semikong-chip-design-llm/discussions).
- See `CONTRIBUTING.md` for guidelines.

Questions? Open an Issue or email [your-email@example.com]. Join us in advancing chip design with AI!
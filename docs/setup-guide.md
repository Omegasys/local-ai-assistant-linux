# Setup Guide

This guide will walk you through the process of setting up the **Local AI Assistant** on your Linux machine. Follow these steps to get started quickly.

## Prerequisites

Before installing the assistant, ensure that your system meets the following requirements:

- **Operating System**: A Linux-based OS (Ubuntu, Fedora, etc.).
- **Python**: Version 3.7 or higher.
- **Dependencies**: Make sure you have `pip` and `git` installed.
- **Optional**: Microphone and speakers for voice interaction.

### Step 1: Clone the Repository

Start by cloning the GitHub repository to your local machine.

```bash
git clone https://github.com/yourusername/local-ai-assistant-linux.git
cd local-ai-assistant-linux
Step 2: Install Dependencies

Install the required Python dependencies using pip:

pip install -r requirements.txt
Step 3: Configure the Assistant

Edit the config.py file to customize the assistant’s behavior, such as setting up voice commands, integrating with the calendar, or modifying privacy settings.

nano src/core/config.py

In the configuration file, you can specify:

Voice Recognition: Enable or disable voice interaction.
Privacy Settings: Adjust the level of data encryption and logging.
Modules: Enable or disable specific modules (e.g., Calendar, File Manager).
Step 4: Start the Assistant

Once the dependencies are installed and configuration is complete, you can start the assistant using the provided script.

./scripts/start_assistant.sh

The assistant will start, and you can interact with it through voice or text commands.

Step 5: (Optional) Autostart on Boot

To have the assistant start automatically when your system boots, follow these additional steps:

Open the crontab file:
crontab -e
Add the following line to the crontab:
@reboot /path/to/your/local-ai-assistant-linux/scripts/start_assistant.sh

Now, your assistant will automatically launch every time you start your computer.

Troubleshooting
Voice Input Not Working: Ensure your microphone is correctly configured. You may need to install additional packages depending on your Linux distribution.
Module Not Loading: Check the config.py file to ensure the module is enabled. You can also run the assistant in debug mode (./scripts/start_assistant.sh --debug) to see detailed error messages.

If you encounter any issues, refer to the GitHub Issues page
 for support.

Congratulations!

You have successfully set up the Local AI Assistant on your Linux machine! You can now interact with your assistant and manage your tasks securely and privately.


---

### `docs/faq.md`:

```markdown
# Frequently Asked Questions (FAQ)

## 1. What is the **Local AI Assistant**?

The **Local AI Assistant** is a privacy-first, AI-driven assistant built to work entirely on your Linux machine. It does not rely on external servers, meaning all data is processed and stored locally, ensuring maximum privacy.

## 2. How does the assistant work?

The assistant uses natural language processing (NLP) to understand user commands and execute actions. You can interact with it through voice or text. It integrates with various Linux tools to handle tasks such as file management, calendar events, and system monitoring.

## 3. Is my data safe?

Yes, your data is kept private. All interactions are processed locally on your machine, and sensitive data is encrypted. The assistant does not share any information with external servers.

## 4. Can I customize the assistant?

Absolutely! You can configure various aspects of the assistant, such as enabling/disabling modules (e.g., calendar, file manager), adjusting privacy settings, and selecting voice or text input.

## 5. What modules are supported?

Currently, the assistant supports the following modules:
- **File Manager**: For interacting with your system's file structure.
- **Calendar**: For managing events and reminders.
- **System Monitor**: For tracking system performance (CPU, RAM, etc.).
- **Networking**: For managing network settings.

## 6. Can I contribute to the project?

Yes, the project is open-source! We welcome contributions through GitHub. Please feel free to open an issue or submit a pull request if you'd like to add new features, fix bugs, or improve documentation.

## 7. How can I disable voice recognition?

If you'd prefer to use the assistant with text input only, you can disable voice recognition in the `config.py` file.

```bash
# Open config.py and set the following to False
VOICE_RECOGNITION_ENABLED = False

const vscode = require("vscode");
const { spawn } = require("child_process");
const path = require("path");

let outputChannel;

/**
 * Resolve python executable per OS
 */
function getPythonCommand() {
	return process.platform === "win32" ? "python" : "python3";
}

/**
 * Run PyShrink as an embedded package (non-interactive)
 */
function runPyShrink(context, args = []) {
	const pythonCmd = getPythonCommand();
	const pyShrinkRoot = context.extensionPath;

	if (!pyShrinkRoot) {
		vscode.window.showErrorMessage("PyShrink engine not found in extension.");
		return;
	}

	outputChannel.appendLine(`\n> pyshrink ${args.join(" ")}`);
	outputChannel.show(true);

	const proc = spawn(
		pythonCmd,
		["-m", "pyshrink", ...args],
		{
			env: {
				...process.env,
				PYTHONPATH: pyShrinkRoot,
				PYTHONIOENCODING: "utf-8",
				PYTHONUTF8: "1"
			}
		}
	);

	proc.stdout.on("data", (data) => {
		outputChannel.appendLine(data.toString());
	});

	proc.stderr.on("data", (data) => {
		outputChannel.appendLine(`ERROR: ${data.toString()}`);
	});

	proc.on("close", (code) => {
		outputChannel.appendLine(`\n✔ PyShrink finished with exit code ${code}\n`);
	});
}

/**
 * Run PyShrink in interactive mode (using terminal for user input)
 */
function runPyShrinkInteractive(context) {
	const pythonCmd = getPythonCommand();
	const pyShrinkRoot = context.extensionPath;

	if (!pyShrinkRoot) {
		vscode.window.showErrorMessage("PyShrink engine not found in extension.");
		return;
	}

	const workspacePath = getWorkspacePath();
	if (!workspacePath) {
		vscode.window.showErrorMessage("No workspace folder opened.");
		return;
	}

	// Create a new integrated terminal
	const terminal = vscode.window.createTerminal({
		name: "PyShrink Interactive",
		env: {
			PYTHONPATH: pyShrinkRoot,
			PYTHONIOENCODING: "utf-8",
			PYTHONUTF8: "1"
		}
	});

	// Show the terminal and run the command with workspace path
	terminal.show();
	terminal.sendText(`${pythonCmd} -m pyshrink --path "${workspacePath}"`);
}

/**
 * Run PyShrink with custom arguments in terminal
 */
function runPyShrinkWithArgs(context, args) {
	const pythonCmd = getPythonCommand();
	const pyShrinkRoot = context.extensionPath;

	if (!pyShrinkRoot) {
		vscode.window.showErrorMessage("PyShrink engine not found in extension.");
		return;
	}

	const workspacePath = getWorkspacePath();
	if (!workspacePath) {
		vscode.window.showErrorMessage("No workspace folder opened.");
		return;
	}

	// Create a new integrated terminal
	const terminal = vscode.window.createTerminal({
		name: "PyShrink",
		env: {
			PYTHONPATH: pyShrinkRoot,
			PYTHONIOENCODING: "utf-8",
			PYTHONUTF8: "1"
		}
	});

	// Show the terminal and run with custom args
	terminal.show();
	terminal.sendText(`${pythonCmd} -m pyshrink --path "${workspacePath}" ${args.join(" ")}`);
}

/**
 * Run PyShrink in full cleanup mode in terminal
 */
function runPyShrinkFullCleanup(context) {
	const pythonCmd = getPythonCommand();
	const pyShrinkRoot = context.extensionPath;

	if (!pyShrinkRoot) {
		vscode.window.showErrorMessage("PyShrink engine not found in extension.");
		return;
	}

	const workspacePath = getWorkspacePath();
	if (!workspacePath) {
		vscode.window.showErrorMessage("No workspace folder opened.");
		return;
	}

	// Create a new integrated terminal
	const terminal = vscode.window.createTerminal({
		name: "PyShrink Full Cleanup",
		env: {
			PYTHONPATH: pyShrinkRoot,
			PYTHONIOENCODING: "utf-8",
			PYTHONUTF8: "1"
		}
	});

	// Show the terminal and run full cleanup
	terminal.show();
	terminal.sendText(`${pythonCmd} -m pyshrink --path "${workspacePath}" --full`);
}

/**
 * Get workspace path safely
 */
function getWorkspacePath() {
	const folder = vscode.workspace.workspaceFolders?.[0];
	return folder ? folder.uri.fsPath : null;
}

/**
 * Extension activation
 */
function activate(context) {
	console.log("✅ PyShrink extension activated");

	outputChannel = vscode.window.createOutputChannel("PyShrink");

	/* -------------------- COMMAND: HELP -------------------- */
	context.subscriptions.push(
		vscode.commands.registerCommand("pyshrink.help", () => {
			runPyShrink(context, ["--help"]);
		})
	);

	/* ---------------- INTERACTIVE MODE ---------------- */
	context.subscriptions.push(
		vscode.commands.registerCommand("pyshrink.interactive", () => {
			runPyShrinkInteractive(context);
		})
	);

	/* -------- RUN WITH ARGUMENTS (--readme, --req) -------- */
	context.subscriptions.push(
		vscode.commands.registerCommand("pyshrink.withArgs", async () => {
			const userArgs = await vscode.window.showInputBox({
				prompt: "Enter PyShrink flags (e.g. --readme --req)",
				placeHolder: "--readme --req"
			});

			if (!userArgs) {
				vscode.window.showWarningMessage("No arguments provided.");
				return;
			}

			const args = userArgs.split(" ").filter(Boolean);
			runPyShrinkWithArgs(context, args);
		})
	);

	/* ---------------- FULL CLEANUP MODE ---------------- */
	context.subscriptions.push(
		vscode.commands.registerCommand("pyshrink.fullCleanup", () => {
			runPyShrinkFullCleanup(context);
		})
	);
}

/**
 * Extension deactivation
 */
function deactivate() {
	console.log("❌ PyShrink extension deactivated");
	if (outputChannel) {
		outputChannel.dispose();
	}
}

module.exports = {
	activate,
	deactivate
};
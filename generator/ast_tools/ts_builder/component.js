const { Project, StructureKind } = require("ts-morph");

const name = process.argv[2];

if (!name) {
    console.error("Usage: node component.js <ComponentName>");
    process.exit(1);
}

const project = new Project({ useInMemoryFileSystem: true });
const file    = project.createSourceFile(`${name}.tsx`);

// ── Import ────────────────────────────────────────────────────────
file.addImportDeclaration({
    moduleSpecifier: "react",
    defaultImport:   "React",
});

// ── Props interface ───────────────────────────────────────────────
file.addInterface({
    name:       `${name}Props`,
    isExported: false,
    properties: [
        {
            name:    "// define your props here",
            type:    "",
            hasQuestionToken: true,
        }
    ],
});

// ── Component function ────────────────────────────────────────────
file.addFunction({
    name:       name,
    isExported: false,
    parameters: [],
    returnType: `React.FC<${name}Props>`,
    statements: [
        `return (
    <div className="flex flex-col items-center justify-center p-4">
      <h1 className="text-2xl font-bold text-gray-800">${name}</h1>
    </div>
  );`,
    ],
});

// ── Export ────────────────────────────────────────────────────────
file.addExportAssignment({
    isExportEquals: false,
    expression:     name,
});

// ── Output ────────────────────────────────────────────────────────
process.stdout.write(file.getFullText());
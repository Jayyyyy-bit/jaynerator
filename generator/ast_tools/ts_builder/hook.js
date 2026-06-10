const { Project } = require("ts-morph");

const name = process.argv[2];
if (!name) { console.error("Usage: node hook.js <HookName>"); process.exit(1); }

const project = new Project({ useInMemoryFileSystem: true });
const file    = project.createSourceFile(`${name}.ts`);

file.addImportDeclaration({
    moduleSpecifier: "react",
    namedImports:    ["useState", "useEffect"],
});

file.addFunction({
    name:       name,
    isExported: false,
    statements: [
        "const [data, setData] = useState(null);",
        "const [loading, setLoading] = useState(false);",
        "const [error, setError] = useState<string | null>(null);",
        `useEffect(() => {
    // your logic here
  }, []);`,
        "return { data, loading, error };",
    ],
});

file.addExportAssignment({ isExportEquals: false, expression: name });
process.stdout.write(file.getFullText());
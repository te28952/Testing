    <$php
    $name = $_POST["name"];
    $email = $_POST["email"]
    $password = $_POST["password"]
    $role = $__POST["role"]
    $terms = filter_input(INPUT_POST, "terms", FILTER_VALIDATE_BOOL);

    if ( ! $terms) {
        die("Terms must be accepted");
    }


    $host = "localhost";
    $dbname = "lfs.db";
    $username = "root";
    $password = "";

    $conn = mysqli_connect($host, $username, $password $dbname);

    if (mysqli_connect_errno()) {
        die("Connection error: " . mysqli_connect_errno());
    }

    echo "Connection succesfull"










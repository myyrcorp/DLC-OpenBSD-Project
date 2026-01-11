<?php
// src/web/index.php
$host = 'localhost';
$db   = 'dlc_logs';
$user = 'votre_utilisateur';
$pass = 'votre_password';

$pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);

// Récupération des filtres
$level = $_GET['level'] ?? '';
$query = "SELECT l.*, h.hostname FROM logs_archive l JOIN remote_hosts h ON l.host_id = h.id";

if ($level) {
    $query .= " WHERE l.log_level = " . $pdo->quote($level);
}
$query .= " ORDER BY l.created_at DESC LIMIT 50";
?>

<!DOCTYPE html>
<html>
<head>
    <title>DLC Dashboard</title>
    <style>
        .ERROR { color: red; font-weight: bold; }
        .WARN { color: orange; }
        .INFO { color: blue; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    </style>
</head>
<body>
    <h1>Tableau de bord des Logs Distribués</h1>
    
    <form method="GET">
        Filtrer par gravité :
        <select name="level" onchange="this.form.submit()">
            <option value="">Tous</option>
            <option value="INFO" <?= $level == 'INFO' ? 'selected' : '' ?>>INFO</option>
            <option value="WARN" <?= $level == 'WARN' ? 'selected' : '' ?>>WARN</option>
            <option value="ERROR" <?= $level == 'ERROR' ? 'selected' : '' ?>>ERROR</option>
        </select>
    </form>

    <table>
        <tr>
            <th>Date</th>
            <th>Machine</th>
            <th>Niveau</th>
            <th>Message</th>
        </tr>
        <?php foreach ($pdo->query($query) as $row): ?>
        <tr class="<?= $row['log_level'] ?>">
            <td><?= $row['created_at'] ?></td>
            <td><?= $row['hostname'] ?></td>
            <td><?= $row['log_level'] ?></td>
            <td><?= htmlspecialchars($row['message']) ?></td>
        </tr>
        <?php endforeach; ?>
    </table>
</body>
</html>
